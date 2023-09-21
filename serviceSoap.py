import zeep
import json

  
  
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
  
  drapeau = client.service.CountryFlag(
    sCountryISOCode=code,
      _soapheaders=[header_value]
  )
  
  codePays = client.service.CountryIntPhoneCode(
      sCountryISOCode=code,
      _soapheaders=[header_value])
      
  capital = client.service.CapitalCity(
    sCountryISOCode=code,
    _soapheaders=[header_value]
  )

  infos =[{'flag' :drapeau,'phone' : codePays, 'capital' : capital}]
  
  return infos

