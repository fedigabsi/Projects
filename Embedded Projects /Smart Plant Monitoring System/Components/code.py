#include <LiquidCrystal_I2C.h>
#include <DHT.h>

LiquidCrystal_I2C lcd (0x27 , 20 , 4) ;
DHT dht (2 , DHT22 ) ; 
int temperature , humidity , light, soltemperature, s, m;

void setup() 
{
  lcd.init();
  dht.begin();  
}

void loop() 
{
  temperature = dht.readTemperature() ;
  humidity = dht.readHumidity() ;
  light = 0.097*analogRead(A1);
  s = analogRead(A0);
  m = map (s,953,115,-24,80);
  soltemperature = m;
  lcd.setCursor( 0 , 0); 
  lcd.print("Temp = "+ String(temperature) + " C");

  lcd.setCursor( 0, 1) ;
  lcd.print("Hum = "+ String(humidity) + " %");

  lcd.setCursor( 0 , 2) ;
  lcd.print("Light = "+ String(light) + " %");

  lcd.setCursor( 0 , 3);
  lcd.print("Sol Temp = "+ String(soltemperature) + " C");

  if (light<30) 
    {
      lcd.backlight();
    }
  else 
    {
      lcd.noBacklight();
    }  
}

