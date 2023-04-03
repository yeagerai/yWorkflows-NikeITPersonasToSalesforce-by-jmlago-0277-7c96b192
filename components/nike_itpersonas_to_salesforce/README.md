
# NikeITPersonasToSalesforce

The NikeITPersonasToSalesforce component connects to the Get Nike IT Personas API using the provided API key and retrieves persona information for a specific department, represented by an industry and department name. The retrieved personas are then sent to Salesforce using the Send Personas to Salesforce component. The output reports whether the data transfer to Salesforce was successful.

## Initial generation prompt
description: "IOs - inputs:\n- class: GetNikeITPersonasInputs\n  fields:\n    api_key:\
  \ str\n    department:\n      industry: str\n      name: str\noutputs:\n- class:\
  \ SendPersonasToSalesforceOutputs\n  fields:\n    success: bool\n"
name: NikeITPersonasToSalesforce


## Transformer breakdown
- Retrieve personas from the Get Nike IT Personas API using the provided API key and the specified department.
- Send the retrieved personas to Salesforce.
- Check if the data transfer to Salesforce was successful.
- Output the result as a boolean value (success).

## Parameters
[]

        