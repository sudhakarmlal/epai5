

def validate(data, template,  current_path=''):
    exception = ''
    key_path = ''
    state = True


    for data_key in data.keys():
        if template.get(data_key):
            pass
        else:
            key_path = f"{current_path}.{data_key}" if current_path else data_key
            exception = f'mismatched keys: {key_path}'
            state = False
            return state, exception


    for key in template.keys():
            key_path = f"{current_path}.{key}" if current_path else key
            print(f'\n\nNow checking the key - {key}')
            value_data = data.get(key, 0)
            value_template = template.get(key, 0)

            #  Check if key exists in the data 
            if value_data:
                #  Check if the value is dict or str
                #  Check if the type value_data and value_template is equal
                #  value_data, value_template

                if isinstance(value_template, dict):
                    # key_path = key_path + "." 
                    
                    if isinstance(value_data, dict):
                        # Recursively check if the two dicts matches
                        state, exception = validate(value_data, value_template, key_path)
                        if exception:
                            state = False
                            break
                    else:
                        exception = f'mismatched keys: {key_path}'
                        state = False
                        break

                
                #  If value is str, then check input values for comparision -->
                else:
                    print('In non dict type filter')
                    print(value_data, value_template)
                    if isinstance(value_data, value_template):
                        print("Type match")
                        # state = True
                        

                    else: 
                        print('type mismatch')
                        exception =  f'bad type: {key_path}'
                        state = False
                        break
                

                        
            else:
                if value_data==None:
                    exception =  f'bad type: {key_path}'
                    state = False
                    
                else:
                    exception = f'mismatched keys: {key_path}'
                    state = False
                break
    return state, exception


# if extra key is sent, then catch and predict
# if not then don't catch and predict