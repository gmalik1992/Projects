import json
import os

from openai import OpenAI

from weather_utilities import (
    get_location_geo_params,
    get_nearby_locations,
    get_weather_report,
)


def add_message(role, content):
    global messages  # Access the global 'messages' list
    messages.append({"role": role, "content": content})
    return messages


tools = [
    {
        "type": "function",
        "description": get_nearby_locations.__doc__,
        "function": {
            "name": "get_nearby_locations",
            "parameters": {
                "type": "object",
                "properties": {"location": {"type": "string"}},
                "required": ["location"],
                "additionalProperties": False,
            },
            "response": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "adm_area1": {
                            "type": "string",
                            "example": "National Capital Territory of Delhi",
                        },
                        "adm_area2": {
                            "type": ["string", "null"],
                            "example": "New Delhi",
                        },
                        "country": {"type": "string", "example": "India"},
                        "lat": {"type": "string", "example": "28.63576N"},
                        "lon": {"type": "string", "example": "77.22445E"},
                        "name": {"type": "string", "example": "New Delhi"},
                        "place_id": {"type": "string", "example": "new-delhi"},
                        "timezone": {"type": "string", "example": "Asia/Kolkata"},
                        "type": {"type": "string", "example": "settlement"},
                    },
                },
            },
        },
    },
    {
        "type": "function",
        "description": get_location_geo_params.__doc__,
        "function": {
            "name": "get_location_geo_params",
            "parameters": {
                "type": "object",
                "properties": {
                    "locations": {"type": "array", "items": {"type": "string"}},
                    "name": {"type": "string", "default": None},
                    "place_id": {"type": "string", "default": None},
                },
                "required": ["locations"],
                "additionalProperties": False,
            },
            "response": {
                "type": "object",
                "properties": {
                    "lat": {"type": "string", "example": "28.63576N"},
                    "lon": {"type": "string", "example": "77.22445E"},
                    "timezone": {"type": "string", "example": "Asia/Kolkata"},
                    "language": {"type": "string", "example": "en"},
                    "units": {
                        "type": "string",
                        "example": "auto",
                        "enum": ["fahrenheit", "celsius"],
                    },
                },
            },
        },
    },
    {
        "type": "function",
        "description": get_weather_report.__doc__,
        "function": {
            "name": "get_weather_report",
            "parameters": {
                "type": "object",
                "properties": {
                    "geo_params": {
                        "type": "object",
                        "properties": {
                            "lat": {"type": "string"},
                            "lon": {"type": "string"},
                            "timezone": {"type": "string"},
                            "language": {"type": "string"},
                            "units": {"type": "string"},
                        },
                    }
                },
                "required": ["geo_params"],
                "additionalProperties": False,
            },
        },
    },
]

available_functions = {
    "get_nearby_locations": get_nearby_locations,
    "get_location_geo_params": get_location_geo_params,
    "get_weather_report": get_weather_report,
}

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

messages = [
    {
        "role": "system",
        "content": "You are a helpful assisitant who for a given location gives weather report and its summary",
    }
]


def get_current_weather_with_llm(user_content):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=add_message("user", user_content),
        tools=tools,
        tool_choice="required",
    )

    # function_reponse = completion.choices[0].message.tool_calls[0].function
    function_reponse = completion.choices[0].message
    if function_reponse.tool_calls:
        function_name = function_reponse.tool_calls[0].function.name
        function_args = json.loads(function_reponse.tool_calls[0].function.arguments)
        weather_function = available_functions.get(function_name)
        call_reponse = weather_function(**function_args)
    return call_reponse
    # print(function_name)
    # print(function_args)


if __name__ == "__main__":
    resp = get_current_weather_with_llm(user_content="What is the weather in Chennai?")
