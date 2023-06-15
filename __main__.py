import os
from openapi_facade import OpenAI
from driver import Driver

def main():
    smm_link = os.getenv("SMM_LINK")
    openai_api_key = os.getenv("OPENAPI_KEY")

    driver = Driver(
        smm_link=smm_link
    )
    openai_facade = OpenAI(
        openai_api_key,
    )

    title = driver.get_tile()
    response = openai_facade.send_request(title.text)
    print(response['choices'][0]['message']['content'])
    driver.quit()   

main()