#Kural Tabanlı Sınıflandırma ile Potansiyel Müşteri Getirisi Hesaplama

#Görev 1: Aşağıdaki Soruları Yanıtlayınız

'''
Soru1 : miuul_gezinomi.xlsx dosyasını okutunuz ve veri seti ile ilgili genel bilgileri gösteriniz..
Soru 2:Kaçunique şehirvardır? Frekanslarınedir?
Soru 3:Kaç unique Concept vardır?
Soru4: Hangi Concept’den kaçar tane satış gerçekleşmiş?
Soru5: Şehirlere göre satışlardan toplam ne kadar kazanılmış?
Soru6: Concept türlerine göre göre ne kadar kazanılmış?
Soru7: Şehirlere göre PRICE ortalamaları nedir?
Soru 8: Conceptlere göre PRICE ortalamaları nedir?
Soru 9: Şehir-Concept kırılımındaPRICE ortalamalarınedir?

'''

#Görev 2: SaleCheckInDayDiff değişkenini kategorik bir değişkene çeviriniz

'''

SaleCheckInDayDiff değişkeni müşterinin CheckIn tarihinden ne kadar önce satin alımını tamamladığını gösterir.
• Aralıkları ikna edici şekilde oluşturunuz.
Örneğin: ‘0_7’, ‘7_30', ‘30_90', ‘90_max’ aralıklarını kullanabilirsiniz.
• Bu aralıklar için "Last Minuters", "Potential Planners", "Planners", "Early Bookers“ isimlerini kullanabilirsiniz.

'''

#Görev 3: COUNTRY, SOURCE, SEX, AGE kırılımında ortalama kazançlar nedir?
'''
Şehir-Concept-EB Score, 
Şehir-Concept- Sezon, 
Şehir-Concept-CInDay kırılımında ortalama ödenen ücret ve yapılan işlem sayısı cinsinden
inceleyiniz ?

'''

import numpy as np
import pandas as pd
import openpyxl 
import matplotlib.pyplot as plt
import seaborn as sbn

#Soru1 : miuul_gezinomi.xlsx dosyasını okutunuz ve veri seti ile ilgili genel bilgileri gösteriniz..

gezinomi=pd.read_excel("miuul_gezinomi.xlsx")
gezinomi_df=pd.DataFrame(gezinomi)
gezinomi_df.info()
gezinomi_df.describe


#Soru 2:Kaç unique şehir vardır? Frekansları nedir?

kol_name=gezinomi_df.columns
gezinomi_df['SaleCityName'].unique()

city_deger=gezinomi_df.SaleCityName.value_counts().values
city_indeks = gezinomi_df.SaleCityName.value_counts().index

gezinomi_df.SaleCityName.value_counts().plot.barh(x=city_deger,y=city_indeks,color='#f4a460')

for i,v in enumerate(city_deger):
    plt.text(v, i, str(v),ha='left', va='center')


#Soru 3:Kaç unique Concept vardır?

kol_name
concept_name=gezinomi_df['ConceptName'].unique()

#Soru4: Hangi Concept’den kaçar tane satış gerçekleşmiş?

concept_satis=gezinomi_df.groupby('ConceptName')['SaleId'].count()
concept_satis_deger=concept_satis.values
concept_satis_index=concept_satis.index

renkler = ['#009acd','#00688b','#87ceeb']
renk=sbn.set_color_codes(palette="colorblind")
plt.figure(figsize=(10,15))
plt.pie(concept_satis_deger,labels=concept_satis_index,data=gezinomi_df,colors=renkler,autopct='%1.1f%%',pctdistance=0.6,textprops={'fontsize':20},labeldistance=1.1)

#Soru5: Şehirlere göre satışlardan toplam ne kadar kazanılmış?

city_sum = gezinomi_df.groupby('SaleCityName')['Price'].sum()
city_sum_deger=city_sum.values
city_sum_key= city_sum.index

fig=plt.figure(figsize=(20,7))
plt.bar(city_sum_key,city_sum_deger,color='#ff1493')

for index, value in zip(city_sum_key,city_sum_deger):
    plt.text(index,value,f'{value}', ha='left', va='bottom', fontsize=14)


x_font={'family':'sans serif','color':'#8b1a1a','fontsize':24}
    
plt.xlabel('Şehirler',fontdict=x_font)

#Soru6: Concept türlerine göre ne kadar kazanılmış?

concept_price=gezinomi_df.groupby('ConceptName')['Price'].sum().plot.line()

fig=plt.figure(figsize=(10,5))
plt.scatter(x=('ConceptName'),y=('Price'),data=gezinomi_df,linewidths=30,c=("green"))
plt.show()

#Soru7: Şehirlere göre PRICE ortalamaları nedir?
#Soru 8: Conceptlere göre PRICE ortalamaları nedir?


plt.figure(figsize=(15,10),dpi=100)
sbn.barplot(gezinomi_df,x='SaleCityName',y='Price',hue='ConceptName',palette="rocket")
plt.legend(bbox_to_anchor =(0.10, 1.10))

gezinomi_df.groupby('SaleCityName')["Price"].mean()

#Soru 9: Şehir-Concept kırılımındaPRICE ortalamaları nedir?

gezinomi_df.groupby(by=['SaleCityName','ConceptName']).agg({"Price":"mean"})

plt.figure(figsize=(15,5))
sbn.color_palette("husl")
sbn.violinplot(gezinomi_df,x='SaleCityName',y="Price",hue='ConceptName',scale_hue=True,gridsize=150,dodge=True,linewidth=2,bw=50,inner="quartile",palette="husl")

#Görev 2: SaleCheckInDayDiff değişkenini kategorik bir değişkene çeviriniz

gezinomi_df.describe()
check=gezinomi_df.SaleCheckInDayDiff
consumer=[]

for i in check:
    if i<7:
        consumer.append("Last Minuters")
        
    elif i<30:
        consumer.append("Potential Planners")
        
    elif i<90:
        consumer.append("Planners")
    
    else:
        consumer.append("Early Bookers")
        
consumer
        
gezinomi_df["ConsumerCategory"] = consumer
gezinomi_df(["ConsumerCategory"],inplace=True)
gezinomi_df["ConsumerCategory"]
gezinomi_df.columns

#Görev 3: COUNTRY, SOURCE, SEX, AGE kırılımında ortalama kazançlar nedir?

#Şehir-Concept-ConsumerCategory
gezinomi_df.groupby(by=['SaleCityName','ConceptName','ConsumerCategory']).agg({"Price":"mean"})

plt.figure(figsize=(15,15))
sbn.catplot(data=gezinomi_df,x='SaleCityName',y="Price",hue='ConceptName',estimator="mean",kind="bar",row='ConsumerCategory',palette="Spectral",aspect=5)

#Şehir-Concept- Sezon, 
gezinomi_df.groupby(by=['SaleCityName','ConceptName','Seasons']).agg({"Price":"mean"})

plt.figure(figsize=(10,10))
sbn.catplot(data=gezinomi_df,x='SaleCityName',y="Price",hue='ConceptName',estimator="mean",kind="bar",row='Seasons',palette="husl",aspect=5)
           

#Şehir-Concept-CInDay kırılımında ortalama ödenen ücret ve yapılan işlem sayısı
gezinomi_df.groupby(by=['SaleCityName','ConceptName','CInDay']).agg({"Price":["mean","count"]})



