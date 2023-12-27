# Amazon Price Tracker

## Requirements 
pip install requests     
pip install bs4

## What is Amazon Price Tracker?
It is a python script implemented using os requests, bs4, lxml, smtplib. It checks if the price of an Amazon item has decreasd over a set target price. If the price has decreased, the script sends an email to the user with the new price and the item's link. 

## How does it work?
<ul>
  <li>
    Step 1 - Use BeautifulSoup to Scrape the Product Price  
    <ol>
      <li> 
        The Amazon item being tracked in this example is a gaming/coding chair.  
        Link to item: https://www.amazon.ca/Fantasylab-Computer-Ergonomic-Adjustable-Support/dp/B0BS144MG4/ref=sr_1_3_sspa?crid=S120KFDEUK4U&keywords=coding%2Bchair&qid=1703652479&sprefix=coding%2Bchari%2Caps%2C133&sr=8-3-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1    
        <img width="1439" alt="Screenshot 2023-12-27 at 2 47 47 AM" src="https://github.com/CoboAr/Amazon-Price-Tracker/assets/144629565/b7c44a8e-25fa-47a5-89ed-93b1c9d9a68a">
      </li> 
      <li>
        Use the requests library to request the HTML page of the Amazon product using the URL the user got from 1.
      </li>
      <li>
        Use BeautifulSoup to make soup with the web page HTML returned back. 
      </li>
      <li>
         Use BeautifulSoup to get hold of the price of the item as a floating point number and print it out.
      </li>
    </ol>
  </li>
  <li>
    Step 2 - Email Alert When Price Below Preset Value
    <ul>
      <li> A website CamelCamelCamle https://camelcamelcamel.com/ it is being used to check the price history of the item.  
        Based on the price history a target price is set. In this case for the coding chair I set it to 350.  
        <img width="1203" alt="Screenshot 2023-12-27 at 2 56 24 AM" src="https://github.com/CoboAr/Amazon-Price-Tracker/assets/144629565/10055c63-74e5-44c4-82da-b4fd161e14a7">   
        <img width="1202" alt="Screenshot 2023-12-27 at 2 57 58 AM" src="https://github.com/CoboAr/Amazon-Price-Tracker/assets/144629565/4d14d2be-b84c-46bf-ba5a-eb55f5ecd3cf">
      </li>
      <li>
        Gmail configuration
        <ul>
         <li> 
            Step 1:  Make sure you've got the correct smtp address for your email provider: smtp.gmail.com
         </li>
         <li>
            Step 2: Go to https://myaccount.google.com/  
            Select Security on the left and scroll down to How you sign in to Google. Enable 2-Step Verification.       
         </li>
          <li>        
            Step 3: Click on 2-Step Verification again, and scroll to the bottom. 
            <ul>
            <li>There you can add an App password.</li>
            <li>Select Other from the dropdown list and enter an app name, e.g. Python Mail, then click Generate.</li>    
            <li>COPY THE PASSWORD - This is the only time you will ever see the password. It is 16 characters with no spaces.</li>
            <li>Use this App password in your Python code instead of your normal password.</li>
          </ul>    
          </li>
          <li>
          Step 4: Add a port number by changing your code to this:       
          smtplib.SMTP("smtp.gmail.com", port=587)
          </li>
        </ul>
      </li>
    </ul>
  </li>
  <li>
    Step 3 - When the actual price of the item is below the target price send an email to the user.
  </li>
</ul>

## Demo

For demonstration purposes I have set the target price to 400. This way when the scrip is run I will receive an email.  

https://github.com/CoboAr/Amazon-Price-Tracker/assets/144629565/83ba2eba-e71e-4a40-a799-d26b43d30681


Enjoy! And please do let me know if you have any comments, constructive criticism, and/or bug reports.
## Author
## Arnold Cobo
