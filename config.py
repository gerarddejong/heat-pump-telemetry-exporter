#!/usr/bin/env python
# 
# Heat Pump Telemetry Exporter Configuration File
#
# Configure the ip of your heat pump here and change the port number you which to use to export metrics.
#
# Update the metrics dictionary below with new values or different value names depending on your heat pump's language configuration.
#
# Original Author: Gerard Diederik de Jong 2023-06-14 
# See: https://github.com/gerarddejong/heat-pump-telemetry-exporter

serverHost = "0.0.0.0"
serverPort = 8888

heatpumpHost = "192.168.2.77"
heatPumpPort = "8214"

metrics = {
    "Temperatures" : [
        {
            "name": "Amb. temp.",
            "help": "The current ambient temperature in degrees celsius. Generally this is the outside temperature.",
            "type": "gauge",
            "variable" : "heat_pump_ambient_temperature"
        },
        {
            "name": "Cur. room temp.",
            "help": "The current room temperature in degrees celsius.",
            "type": "gauge",
            "variable" : "heat_pump_current_room_temperature"
        },
        {
            "name": "Act. service water ", # Note the space charater at the end.
            "help": "The actual service water temperature in degrees celsius. The current temperature of water supplying hot water taps. ",
            "type": "gauge",
            "variable" : "heat_pump_actual_service_water_temperature"
        },
        {
            "name": "Targ. service water",
            "help": "The target service water temperature in degrees celsius.",
            "type": "gauge",
            "variable" : "heat_pump_target_service_water_temperature"
        },
        {
            "name": "Flow",
            "help": "The flow temperature in degrees celsius. The flow temperature refers to the temperature of the water in the supply (flow) pipe in a heating system or separate part of a heating system.",
            "type": "gauge",
            "variable" : "heat_pump_flow_temperature"
        },
        {
            "name": "Return",
            "help": "The return temperature in degrees celsius. The return temperature is the temperature of the water in the pipe system after heat has been released into the building. The difference between inlet temperature and return temperature of the water occurs during transport through the heating system.",
            "type": "gauge",
            "variable" : "heat_pump_return_temperature"
        },
        {
            "name": "Targeted return",
            "help": "The target return temperature in degrees celsius.",
            "type": "gauge",
            "variable" : "heat_pump_target_return_temperature"
        },
        {
            "name": "hot gas",
            "help": "The hot gas temperature in degrees celsius.",
            "type": "gauge",
            "variable" : "heat_pump_hot_gas_temperature"
        },
        {
            "name": "Heat source in",
            "help": "The input heat source temperature in degrees celsius.",
            "type": "gauge",
            "variable" : "heat_pump_input_heat_source_temperature"
        },
        {
            "name": "Intake compressor",
            "help": "The intake compressor temperature in degrees celsius.",
            "type": "gauge",
            "variable" : "heat_pump_intake_compressor_temperature"
        },
        {
            "name": "Intake vapor",
            "help": "The intake vapor temperature in degrees celsius.",
            "type": "gauge",
            "variable" : "heat_pump_intake_vapor_temperature"
        }
    ],
    "Output status" : [
        {
            "name": "floor heat. pump 1",
            "help": "Floor heating, pump 1 status (0=Off 1=On).",
            "type": "gauge",
            "variable" : "heat_pump_floor_heat_pump_1_status"
        },
        {
            "name": "DHW pump",
            "help": "Domestic Hot Water (DHW) pump status (0=Off 1=On).",
            "type": "gauge",
            "variable" : "heat_pump_domestic_hot_water_pump_status"
        },
        {
            "name": "heat. sys. pump",
            "help": "Heat system pump status (0=Off 1=On).",
            "type": "gauge",
            "variable" : "heat_pump_heat_system_pump_status"
        },
        {
            "name": "Compressor",
            "help": "Compressor status (0=Off 1=On).",
            "type": "gauge",
            "variable" : "heat_pump_compressor_status"
        },
        {
            "name": "suppl. pump ", # Note the space charater at the end.
            "help": "Supply pump status (0=Off 1=On).",
            "type": "gauge",
            "variable" : "heat_pump_supply_pump_status"
        },
        {
            "name": "2nd heat gen. 1",
            "help": "Second heat generator 1 status (e.g. electric heating element) in the storage tank (0=Off 1=On).",
            "type": "gauge",
            "variable" : "heat_pump_2nd_heat_generator_1_status"
        }
    ],
    "Output status" : [
        {
            "name": "2nd heat gen. 1",
            "help": "Second heat generator 1 status (e.g. electric heating element) in the storage tank (0=Off 1=On).",
            "type": "gauge",
            "variable" : "heat_pump_2nd_heat_generator_1_status"
        }
    ]
}