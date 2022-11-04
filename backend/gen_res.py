import requests


def main():
    q = ['1001', '1002', '1003', '1004', '1005', '1006', '1501', '1502', '1503', '1504', '1505', '1701', '1702', '1703', '1704', '1705', '1706', '1707', '1709', '1711', '2701', '2702', '2703', '2704', '2705', '2706', '2707', '2708', '3702', '3704', '3705', '3793', '3795', '3796', '3797', '3798', '4701', '4702', '4703', '4704', '4705', '4706', '4707', '4708', '4709', '4710', '4712', '4713', '4714', '4716', '4798', '4799', '5794', '5795', '5797', '5798', '5799', '6701', '6703', '6704', '6705', '6706', '6708', '6710', '6711', '6712', '6713', '6714', '6715', '6716', '7791', '7793', '7794', '7795', '7796', '7797', '7798', '8701', '8702', '8704', '8706', '9701', '9702', '9703', '9704', '9705', '9706']
    url = "http://localhost:5000/api/v1/density"

    while True:
        id = q.pop(0)
        # add back to the end
        q.append(id)
        
        # make API call
        params = {"cameraID": id}
        r = requests.get(url, params)
        try:
            out = r.json()
            print(f"Inference for {id} done. Output: {out}")
        except: 
            print("Inference failed, no response from backend")

if __name__ == "__main__":
    main()
