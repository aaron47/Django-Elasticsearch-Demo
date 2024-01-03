"""
Make sure you add this to your settings py

- Default is for your local elasticsearch
- Cloud is for your cloud based elasticsearch on elastic.co
"""

ELASTICSEARCH_DSL = {
    "default": {
        "hosts": "https://127.0.0.1:9200/",
        "http_auth": ("elastic", ""),
        "ca_certs": "path/to/your/certs",
    },
    "cloud": {
		"cloud_id": "",
		"http_auth": ("elastic", "")
    }
}