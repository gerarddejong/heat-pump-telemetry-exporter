#!/usr/bin/env python
# 
# Heat Pump Telemetry Exporter
#
# Original Author: Gerard Diederik de Jong 2023-06-14
# See: https://github.com/gerarddejong/heat-pump-telemetry-exporter

import websocket
import xml.etree.ElementTree as ET
import re
from http.server import BaseHTTPRequestHandler, HTTPServer
import time

import config 

class HeatPumpTelemetry:
    def getMetrics(self):
        metricsString = ""
        
        #websocket.enableTrace(True)
        webSocketConnection = websocket.WebSocket()
        webSocketConnection.connect("ws://%s:%s/" % (config.heatPumpHost, config.heatPumpPort), subprotocols=["Lux_WS"])

        webSocketConnection.send("LOGIN;0")
        loginResponseString = webSocketConnection.recv()
        navigationMenuXML = ET.fromstring(loginResponseString)

        for group in list(config.metrics.keys()):
            menuOptionId = self.__getItemId(group, navigationMenuXML)
            webSocketConnection.send("GET;%s" % menuOptionId)
            contentResponseString = webSocketConnection.recv()
            contentXML = ET.fromstring(contentResponseString)
            for metric in config.metrics[group]:
                metricsString += self.__getHelpTypeAndValue(self, metric, contentXML)

        webSocketConnection.close()
        return metricsString
    
    def __getHelpTypeAndValue(self, metric, contentXML):
        metricData = ""
        metricValue = self.__getMetric(metric["name"], contentXML)
        metricData += "# HELP %s %s\n" % (metric["variable"], metric["help"])
        metricData += "# TYPE %s %s\n" % (metric["variable"], metric["type"])
        metricData += "%s %s\n" % (metric["variable"], self.__removeUnits(metricValue))
        return metricData

    def __getItemId(name, navigationMenuXML):
        for navigationItem in navigationMenuXML:
            for menuItem in navigationItem:
                for menuItemOption in menuItem:
                    if menuItemOption.tag == "name" and menuItemOption.text == name:
                        return menuItem.attrib["id"]
        return None

    def __getMetric(name, contentXML):
        for item in contentXML:
            if item.tag == "item":
                itemName = item.find("name").text
                itemValue = item.find("value").text
                if itemName == name: 
                    return itemValue
        return None

    def __removeUnits(valueString):
        valueString = valueString.replace("On", "1")
        valueString = valueString.replace("Off", "0")
        return re.sub("[^0-9.]", "", valueString)    

class MetricsServer(BaseHTTPRequestHandler):
    def do_GET(self):
        if "/metrics" in self.path:
            telemetryDiagnosticsRetrievalTime = time.time()
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()

            metricsResponseString = HeatPumpTelemetry.getMetrics(HeatPumpTelemetry)

            if "telemetry_diagnostics=true" in self.path:
                metricsResponseString += "# HELP heat_pump_telemetry_retrieval_time The time taken to retrieve telemetry data from the heat pump in seconds. This is useful for diagnostics and troubleshooting time out issues.\n"
                metricsResponseString += "# TYPE heat_pump_telemetry_retrieval_time gague\n"
                metricsResponseString += "heat_pump_telemetry_diagnostics_retrieval_time %.2f\n" % (time.time() - telemetryDiagnosticsRetrievalTime)
            
            self.wfile.write(bytes(metricsResponseString, "utf-8"))
        
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(bytes("<html><title>Heat Pump Telemetry Exporter</title><body><p>Error! Resource not found.</p><p>Navigate to <a href='/metrics'>/metrics</a> for telemetry data compatible with Prometheus.</p></body></html>", "utf-8"))
        
if __name__ == "__main__":
    webServer = HTTPServer((config.serverHost, config.serverPort), MetricsServer)
    print("Heat Pump Telemetry Server started http://%s:%s" % (config.serverHost, config.serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
