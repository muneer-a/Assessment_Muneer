import re

sample_data =  { 
    "tables": [ 
        { 
            "name": "customers", 
            "columns": [ 
                { 
                    "name": "customer_id", 
                    "type": "string", 
                    "required": True, 
                    "validation": { 
                        "pattern": "^CUS[0-9]{6}$" 
                    } 
                }, 
                { 
                    "name": "purchase_amount", 
                    "type": "decimal", 
                    "required": True, 
                    "validation": { 
                        "min": 0, 
                        "max": 1000000 
                    } 
                } 
            ] 
        } 
    ] 
}

def extract_columns(sample_data):
    schema_mapping ={}
    for table in sample_data['tables']:
        schema_mapping['name']=table['columns']
    return schema_mapping


def validate_schema(table_name,data,schema):
    columns = schema.get(table_name,[])
    errors=[]
    for col in columns:
        col_name = col['name']
        col_type = col['type']
        col_req = col['required']
        validation = col.get('validation',{})

        if col_req and col_name not in data :
            errors.append(f"{table_name}.{col_name} is required but missing")
            continue

    value = col.get(col_name)

    if col_type == 'string' and not isinstance(value,str):
        errors.append(f"{table_name}.{col_name} must be a string")
    elif col_type == 'decimal' and not isinstance(value,float):
        errors.append(f"{table_name}.{col_name} must be a decimal")

    if 'pattern' in validation and isinstance(value,'str'):
        if not re.match(validation['pattern'],value):
            errors.append(f"{table_name}.{col_name} does not match pattern {validation['pattern']}")
        
    if "min" in validation and isinstance(value, (int, float)):
        if value < validation["min"]:
            errors.append(f"{table_name}.{col_name} is below the minimum value {validation['min']}")
    if "max" in validation and isinstance(value, (int, float)):
        if value > validation["max"]:
            errors.append(f"{table_name}.{col_name} exceeds the maximum value {validation['max']}")

    return errors

def sort_errors(errors):
    return sorted(errors)