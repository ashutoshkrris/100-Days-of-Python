from spider import get_latest_price
import smtplib

BUY_PRICE = 1000

product_url = input("Enter the product page link : ")

product_details = get_latest_price(product_url)

if product_details == "Couldn't extract data":
    print("There was error extracting the data.")
else:
    if product_details['price'] < BUY_PRICE:
        message = f"{product_details['title']} is now available at Rs. {product_details['price']}"

        with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
            connection.starttls()
            result = connection.login('email@gmail.com', 'password')
            connection.sendmail(
                from_addr='',
                to_addrs='',
                msg=f"Subject:Amazon Price Alert!\n\n{message}\n\nProduct Page : {product_url}"
            )
        print("Email has been sent")
    else:
        print("The latest price is more than the BUY PRICE.")
