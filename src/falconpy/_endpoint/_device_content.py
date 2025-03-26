"""Internal API endpoint constant library.

 _______                        __ _______ __        __ __
|   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
|.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
|.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
|:  1   |                         |:  1   |
|::.. . |   CROWDSTRIKE FALCON    |::.. . |    FalconPy
`-------'                         `-------'

OAuth2 API - Customer SDK

This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or
distribute this software, either in source code form or as a compiled
binary, for any purpose, commercial or non-commercial, and by any
means.

In jurisdictions that recognize copyright laws, the author or authors
of this software dedicate any and all copyright interest in the
software to the public domain. We make this dedication for the benefit
of the public at large and to the detriment of our heirs and
successors. We intend this dedication to be an overt act of
relinquishment in perpetuity of all present and future rights to this
software under copyright law.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.

For more information, please refer to <https://unlicense.org>
"""

_device_content_endpoints = [
  [
    "entities_states_v1",
    "GET",
    "/device-content/entities/states/v1",
    "Retrieve the host content state for a number of ids between 1 and 100.",
    "device_content",
    [
      {
        "type": "array",
        "items": {
          "type": "string"
        },
        "collectionFormat": "multi",
        "description": "The ids of the devices to fetch the content state of.",
        "name": "ids",
        "in": "query",
        "required": True
      }
    ]
  ],
  [
    "queries_states_v1",
    "GET",
    "/device-content/queries/states/v1",
    "Query for the content state of the host.",
    "device_content",
    [
      {
        "maximum": 10000,
        "minimum": 1,
        "type": "integer",
        "default": 100,
        "description": "The max number of resource ids to return.",
        "name": "limit",
        "in": "query"
      },
      {
        "type": "string",
        "default": "last_seen.desc",
        "description": "What field to sort the results on.",
        "name": "sort",
        "in": "query"
      },
      {
        "type": "integer",
        "description": "The offset token returned from the previous query.\nIf none was returned, there are no "
        "more pages to the result set.",
        "name": "offset",
        "in": "query"
      },
      {
        "type": "string",
        "description": "The FQL search filter",
        "name": "filter",
        "in": "query"
      }
    ]
  ]
]
