import zeep
import json
  
# # set the WSDL URL
# wsdl_url = "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso?WSDL"
  
# # set method URL
# method_url = "http://webservices.oorsprong.org/websamples.countryinfo/CountryIntPhoneCode"
# # set service URL
# service_url = "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso"
  
# # create the header element
# header = zeep.xsd.Element(
#     "Header",
#     zeep.xsd.ComplexType(
#         [
#             zeep.xsd.Element(
#                 "{http://www.w3.org/2005/08/addressing}Action", zeep.xsd.String()
#             ),
#             zeep.xsd.Element(
#                 "{http://www.w3.org/2005/08/addressing}To", zeep.xsd.String()
#             ),
#         ]
#     ),
# )
# # set the header value from header element
# header_value = header(Action=method_url, To=service_url)
  
# # initialize zeep client
# client = zeep.Client(wsdl=wsdl_url)

# # variable d'entrée du programme
# pays_code ="GA"
  

# result = client.service.CountryFlag(
#   sCountryISOCode=pays_code,
#     _soapheaders=[header_value]
# )
# print(f"Flag  for {pays_code} is {result}")
  
# # make the service call
# result = client.service.CountryIntPhoneCode(
#     sCountryISOCode=pays_code,
#     _soapheaders=[header_value]
# )
# print(f"Phone Code for {pays_code} is {result}")
  

# result = client.service.CapitalCity(
#   sCountryISOCode=pays_code,
#     _soapheaders=[header_value]
# )

# print(f"Capital for {pays_code} is {result}")
  
  
def Infos_pays(code):
  wsdl_url = "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso?WSDL"
  method_url = "http://webservices.oorsprong.org/websamples.countryinfo/CountryIntPhoneCode"
  service_url = "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso"
  header = zeep.xsd.Element(
      "Header",
      zeep.xsd.ComplexType(
          [
              zeep.xsd.Element(
                  "{http://www.w3.org/2005/08/addressing}Action", zeep.xsd.String()
              ),
              zeep.xsd.Element(
                  "{http://www.w3.org/2005/08/addressing}To", zeep.xsd.String()
              ),
          ]
      ),
  )
  header_value = header(Action=method_url, To=service_url)
  client = zeep.Client(wsdl=wsdl_url)
  
  result1 = client.service.CountryFlag(
    sCountryISOCode=code,
      _soapheaders=[header_value]
  )
  
  result2 = client.service.CountryIntPhoneCode(
      sCountryISOCode=code,
      _soapheaders=[header_value])
      
  result3 = client.service.CapitalCity(
    sCountryISOCode=code,
    _soapheaders=[header_value]
  )
  # json.dumps(key1=result1 ,
  # key2=result2,
  # key3=result3)
  infos =[{'flag' :result1,'phone' : result2, 'capital' : result3}]
  
  return infos


#Infos_pays('BZ')