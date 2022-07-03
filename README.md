0. Target an available IAM or Cloud Foundry namespace.
```bash
    ibmcloud fn namespace target NAMESPACE
```


1. Cloning repo:
```bash
    git clonde https://github.com/svyatjes/ibm_cloud
    cd ibm_cloud
```

2. Create action
```bash
    ibmcloud fn action create act_name main.py
```

3. Update an action
```bash
    ibmcloud fn action update act_name --web true
```

4. Create API:
```bash
    ibmcloud fn api create /get_currency /currency post act_name --response-type json
```