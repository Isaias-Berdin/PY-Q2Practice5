from pyscript import document, display

def check_country(e):
    country = {
       "ph" : "Philippines",
       "ic" : "Iceland",
       "ge" : "Germany",
       "ng" : "Nigeria",
       "us" : "United States of America"
    }  
 
    country_code = document.getElementById("cries").value
    
    country["it"] = "Italy" #ADDS. THAT. THANG. UPPP
    display(country.get(country_code, "Country code NOT found, don't even try again."), target="output1")
    
def show_country(e):
    document.getElementById("output1").innerHTML = ""
    country = {
       "ph" : "Philippines",
       "ic" : "Iceland",
       "ge" : "Germany",
       "ng" : "Nigeria",
       "us" : "United States of America"
    }  
    
    country_code = document.getElementById("cries").value
    
    show_country = country_code in country
    list_country = list(country.keys())
    
    display("The number of countries are", len(country), target="output1")
    display("Is it in the dictionary?", show_country, target="output1")
    display("What ARE the countries?", list_country, target="output1")