def bubble(arr):
    n=len(arr) 
    for i in range(n-2,-1,-1):
        swap=False
        for j in range(0,i+1):    
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swap=True        

        if swap==False: 
            return arr
         
 
    return arr
