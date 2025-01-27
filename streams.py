initial_streams = int(input("How many streams? "))

flows = []
for i in range(initial_streams):
    flow = int(input(f"What's the flow of stream {i+1}: "))
    flows.append(flow)
    
while True:
    no = int(input("99, 88 or 77: "))
    if no == 77:
        break
    
    elif no == 99:
        stream_no = int(input("Which stream? "))      
        percentage = float(input("%? "))   
        
        ratio = percentage/100
        old_flow = flows[stream_no-1]  
        
        left_flow = old_flow * ratio
        right_flow = old_flow - left_flow
        
        flows[stream_no-1] = left_flow
        flows.insert(stream_no, right_flow)
    
    elif no == 88:
        stream_no = int(input("Which stream? "))
        flows[stream_no-1] = flows[stream_no-1] + flows[stream_no]
        del flows[stream_no]
        
final_flows = [int(round(f)) for f in flows]
answer = ''
for i in final_flows:
    answer = answer + str(flow) + ' '
print(answer)