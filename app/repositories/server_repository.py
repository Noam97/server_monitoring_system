{
  "info": {
    "name": "Server Monitoring System - Grouped by Protocol",
    "schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json"
  },
  "item": [
    {
      "name": "HTTP",
      "item": [
        {
          "name": "Create HTTP Server",
          "request": {
            "method": "POST",
            "header": [
              { "key": "Content-Type", "value": "application/json" }
            ],
            "body": {
              "mode": "raw",
              "raw": "{\n  \"name\": \"Example HTTP\",\n  \"url\": \"example.com\",\n  \"protocol\": \"http\"\n}"
            },
            "url": {
              "raw": "http://localhost:8000/servers",
              "protocol": "http",
              "host": ["localhost"],
              "port": "8000",
              "path": ["servers"]
            }
          }
        },
        {
          "name": "Was HTTP Server Healthy at Timestamp",
          "request": {
            "method": "GET",
            "url": {
              "raw": "http://localhost:8000/servers/was-healthy/1?timestamp=2025-07-14T12:00:00",
              "protocol": "http",
              "host": ["localhost"],
              "port": "8000",
              "path": ["servers", "was-healthy", "1"],
              "query": [
                { "key": "timestamp", "value": "2025-07-14T12:00:00" }
              ]
            }
          }
        }
      ]
    },
    {
      "name": "HTTPS",
      "item": [
        {
          "name": "Create HTTPS Server",
          "request": {
            "method": "POST",
            "header": [
              { "key": "Content-Type", "value": "application/json" }
            ],
            "body": {
              "mode": "raw",
              "raw": "{\n  \"name\": \"Google\",\n  \"url\": \"www.google.com\",\n  \"protocol\": \"https\"\n}"
            },
            "url": {
              "raw": "http://localhost:8000/servers",
              "protocol": "http",
              "host": ["localhost"],
              "port": "8000",
              "path": ["servers"]
            }
          }
        },
        {
          "name": "Create HTTPS Server - Invalid URL",
          "request": {
            "method": "POST",
            "header": [
              { "key": "Content-Type", "value": "application/json" }
            ],
            "body": {
              "mode": "raw",
              "raw": "{\n  \"name\": \"invalid\",\n  \"url\": \"google.example\",\n  \"protocol\": \"https\"\n}"
            },
            "url": {
              "raw": "http://localhost:8000/servers",
              "protocol": "http",
              "host": ["localhost"],
              "port": "8000",
              "path": ["servers"]
            }
          }
        },
        {
          "name": "Was HTTPS Server Healthy at Timestamp",
          "request": {
            "method": "GET",
            "url": {
              "raw": "http://localhost:8000/servers/was-healthy/1?timestamp=2025-07-14T12:00:00",
              "protocol": "http",
              "host": ["localhost"],
              "port": "8000",
              "path": ["servers", "was-healthy", "1"],
              "query": [
                { "key": "timestamp", "value": "2025-07-14T12:00:00" }
              ]
            }
          }
        }
      ]
    },
    {
      "name": "FTP",
      "item": [
        {
          "name": "Create FTP Server - Valid",
          "request": {
            "method": "POST",
            "header": [
              { "key": "Content-Type", "value": "application/json" }
            ],
            "body": {
              "mode": "raw",
              "raw": "{\n  \"name\": \"Rebex FTP\",\n  \"url\": \"test.rebex.net\",\n  \"protocol\": \"ftp\",\n  \"credentials\": {\n    \"username\": \"demo\",\n    \"password\": \"password\"\n  }\n}"
            },
            "url": {
              "raw": "http://localhost:8000/servers",
              "protocol": "http",
              "host": ["localhost"],
              "port": "8000",
              "path": ["servers"]
            }
          }
        },
        {
          "name": "Create FTP Server - Invalid Login",
          "request": {
            "method": "POST",
            "header": [
              { "key": "Content-Type", "value": "application/json" }
            ],
            "body": {
              "mode": "raw",
              "raw": "{\n  \"name\": \"DLptest Bad\",\n  \"url\": \"dlptest.com\",\n  \"protocol\": \"ftp\",\n  \"credentials\": {\n    \"username\": \"bad\",\n    \"password\": \"bad\"\n  }\n}"
            },
            "url": {
              "raw": "http://localhost:8000/servers",
              "protocol": "http",
              "host": ["localhost"],
              "port": "8000",
              "path": ["servers"]
            }
          }
        },
        {
          "name": "Was FTP Server Healthy at Timestamp",
          "request": {
            "method": "GET",
            "url": {
              "raw": "http://localhost:8000/servers/was-healthy/1?timestamp=2025-07-14T12:00:00",
              "protocol": "http",
              "host": ["localhost"],
              "port": "8000",
              "path": ["servers", "was-healthy", "1"],
              "query": [
                { "key": "timestamp", "value": "2025-07-14T12:00:00" }
              ]
            }
          }
        }
      ]
    }
  ]
}
