class PCraftPlugin(object):
    name = "MakeVariables"
    
    def __init__(self, session, plugins_data):
        self.plugins_data = plugins_data

    def help(self):
        helpstr="""
This Plugins creates variables from scractch based on the [pcraft Taxonomy][taxonomy].

### Example

To replace the two variables "ip-dst" and "domain" that any previous plugins may have
built, the following can be written:

```
buildvars:
  _plugin: MakeVariables

  ip-dst: "1.1.1.1"
  domain: "www.example.com"

  _next: dnsconnect
```

[taxonomy]:taxonomy.md
"""
        return helpstr
        
    def run(self, script=None):
        if script:
            for k, v in script.items():
                if not k.startswith("_"):
                    self.plugins_data._set(k, v)
            return script["_next"], self.plugins_data
        print("Error with MakeVariables, no script provided!")
        
