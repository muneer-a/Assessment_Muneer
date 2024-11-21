

import pandas as pd

def  parse_log_line(lines) :
    timestamp, ip, status_code, endpoint=line.strip().split(',')
    return (timestamp, ip, status_code, endpoint)

def get_unique_visitors(logs):
    return len(pd.unique(logs['ip']))

def get_popular_endpoints(logs, top_n=5) :
    series1=logs['endpoint'].value_counts().head(5)
    return list(zip(series1.index,series1))

#def get_error_rate(logs) :
#    count=len(logs['status_code'].str.startswith('4'|'5'))
#    total= len(logs['status_code']
#    return float((count/total)*100)

def generate_report(filename): 
    data=[]
    with open(filename,'r') as f:
        
        for line in f:
            data.append(parse_log_line(line))
        print(data)
    log = pd.DataFrame(data, columns =['timestamp', 'ip', 'status_code','endpoint'])
            
    
    print(f"Count of Unique IP Addresses : {get_unique_visitors(log)}")            
    print(f"Most accessed Endpoints : {get_popular_endpoints(log)}")
    #print(f"Error rate Percentage:{get_error_rate(log)}")
if __name__ == '__main__':
    filename = 'sample-log.txt'
    
            
    generate_report(filename)
 
