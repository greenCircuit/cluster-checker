import os, json, requests
import xml.etree.ElementTree as ET

def parse_json()->str:
    message = ""

    json_files = [filename for filename in os.listdir("./") if filename.endswith('.json')]
    for file in json_files:
        with open(file, 'r') as file:
            data = file.read()
        data = json.loads(data)
        for failed in data.get("failed"):
            message += "Failed object: %s %s, Namespace: %s, msg: %s \n" % (failed.get("object"), failed.get("name"), failed.get("ns"), failed.get("condition"))
    if message == "":
        return "PASS: no errors in json"
    return message

def parse_output_xml():
# Load Robot Framework output.xml
    tree = ET.parse('output.xml')
    root = tree.getroot()

    # Robot Framework defines <suite> which contains <test>
    message = ""

    for suite in root.findall('suite'):
        tests = suite.iter("test")        
        for test in tests:
            name = test.attrib.get('name')
            status_element = test.find('status')
            if status_element is not None:
                status = status_element.attrib.get('status')  # 'PASS' or 'FAIL'
                if status == 'FAIL':
                    message += (status + ": " + name + " \n") 

        
    if message == "":
        return "✅✅✅ PASS: no errors in tests ✅✅✅"

    return message

def send_slack():
    prepend = "Robot Test Report* :robot_face:\n"
    final_message = prepend + "\n" + parse_output_xml() + "\n" + parse_json()
    print("Final message will look like" + "\n" + final_message)
    webhook_url = os.environ["SLACK_URL"]
    # message_text = f"*Robot Framework Test Summary*\n• ✅"
    payload = {'text': final_message}
    response = requests.post(
        webhook_url, data=json.dumps(payload),
        headers={'Content-Type': 'application/json'}
    )
    if response.status_code == 200:
        print('Notification sent successfully.')
    else:
        print(f'Failed to send notification. Status code: {response.status_code}, Response: {response.text}')

# sending notification only when env specified 
if os.environ["NOTIFY"] == "true":    
    send_slack()
