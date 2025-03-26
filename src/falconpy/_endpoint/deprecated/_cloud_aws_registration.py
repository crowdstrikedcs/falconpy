"""Internal API endpoint constant library (deprecated operations).

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

_cloud_aws_registration_endpoints = [
  [
    "cloud-registration-aws-get-accounts",
    "GET",
    "/cloud-security-registration-aws/entities/account/v1",
    "Retrieve existing AWS accounts by account IDs",
    "cloud_aws_registration",
    [
      {
        "type": "array",
        "items": {
          "type": "string"
        },
        "collectionFormat": "multi",
        "description": "AWS account IDs to filter",
        "name": "ids",
        "in": "query"
      }
    ]
  ],
  [
    "cloud-registration-aws-create-account",
    "POST",
    "/cloud-security-registration-aws/entities/account/v1",
    "Creates a new account in our system for a customer.",
    "cloud_aws_registration",
    [
      {
        "name": "body",
        "in": "body",
        "required": True
      }
    ]
  ],
  [
    "cloud-registration-aws-update-account",
    "PATCH",
    "/cloud-security-registration-aws/entities/account/v1",
    "Patches a existing account in our system for a customer.",
    "cloud_aws_registration",
    [
      {
        "name": "body",
        "in": "body",
        "required": True
      }
    ]
  ],
  [
    "cloud-registration-aws-delete-account",
    "DELETE",
    "/cloud-security-registration-aws/entities/account/v1",
    "Deletes an existing AWS account or organization in our system.",
    "cloud_aws_registration",
    [
      {
        "type": "array",
        "items": {
          "type": "string"
        },
        "collectionFormat": "multi",
        "description": "AWS account IDs to remove",
        "name": "ids",
        "in": "query"
      },
      {
        "type": "array",
        "items": {
          "type": "string"
        },
        "collectionFormat": "multi",
        "description": "AWS organization IDs to remove",
        "name": "organization-ids",
        "in": "query"
      }
    ]
  ],
  [
    "cloud-registration-aws-validate-accounts",
    "POST",
    "/cloud-security-registration-aws/entities/account/validate/v1",
    "Validates the AWS account in our system for a provided CID. For internal clients only.",
    "cloud_aws_registration",
    [
      {
        "type": "string",
        "description": "Product registered for an account",
        "name": "products",
        "in": "query",
        "required": True
      },
      {
        "type": "array",
        "items": {
          "type": "string"
        },
        "collectionFormat": "csv",
        "description": "Features registered for an account",
        "name": "feature",
        "in": "query",
        "required": True
      },
      {
        "pattern": "^\\d{12}$",
        "type": "string",
        "description": "AWS Account ID",
        "name": "account-id",
        "in": "query"
      },
      {
        "pattern": "^arn:aws:iam::\\d{12}:role/.+",
        "type": "string",
        "description": "IAM Role ARN",
        "name": "iam-role-arn",
        "in": "query"
      }
    ]
  ],
  [
    "cloud-registration-aws-query-accounts",
    "GET",
    "/cloud-security-registration-aws/queries/account/v1",
    "Retrieve existing AWS accounts by account IDs",
    "cloud_aws_registration",
    [
      {
        "type": "array",
        "items": {
          "type": "string"
        },
        "collectionFormat": "multi",
        "description": "Organization IDs used to filter accounts",
        "name": "organization-ids",
        "in": "query"
      },
      {
        "type": "array",
        "items": {
          "type": "string"
        },
        "collectionFormat": "multi",
        "description": "Products registered for an account",
        "name": "products",
        "in": "query",
        "required": True
      },
      {
        "type": "array",
        "items": {
          "type": "string"
        },
        "collectionFormat": "multi",
        "description": "Features registered for an account",
        "name": "features",
        "in": "query",
        "required": True
      },
      {
        "enum": [
          "provisioned",
          "operational"
        ],
        "type": "string",
        "description": "Account status to filter results by.",
        "name": "account-status",
        "in": "query"
      },
      {
        "maximum": 500,
        "minimum": 0,
        "type": "integer",
        "default": 100,
        "description": "The maximum number of items to return. When not specified or 0, 100 is used. When "
        "larger than 500, 500 is used.",
        "name": "limit",
        "in": "query"
      },
      {
        "type": "integer",
        "description": "The offset to start retrieving records from.",
        "name": "offset",
        "in": "query"
      },
      {
        "enum": [
          "organization"
        ],
        "type": "string",
        "description": "Field to group by.",
        "name": "group_by",
        "in": "query"
      }
    ]
  ]
]
