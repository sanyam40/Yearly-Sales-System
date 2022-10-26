import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# submenu1 to Display Data
def submenu1():
    op1=0
    while op1!=7:
        print('1. Display All Columns and range of index')
        print('2. Reading complete CSV file')
        print('3. Reading complete CSV file without index')
        print('4. Showing Quarterly Sales')
        print('5. Showing data for specific month')
        print('6. Duplicating Data into new CSV file')
        print('7. Go back to main menu')
        print()
        op1=int(input('Enter choice to Display Data'))
        print()
        if op1==1:
            df=pd.read_csv('E:\\projects\\Yearly Sales Analysis project\\Yearlysales.csv')
            print(df.columns)
            print(df.index)
        if op1==2:
            df=pd.read_csv('E:\\projects\\Yearly Sales Analysis project\\Yearlysales.csv')
            print(df)
        if op1==3:
            df=pd.read_csv('E:\\projects\\Yearly Sales Analysis project\\Yearlysales.csv',index_col=0)
            print(df)
        if op1==4:
            df=pd.read_csv('E:\\projects\\Yearly Sales Analysis project\\Yearlysales.csv',usecols=['Quarter','Sales'])
            print(df)       
        if op1==5:
            df=pd.read_csv('E:\\projects\\Yearly Sales Analysis project\\Yearlysales.csv')
            n=input('Enter the Month Name to display the details(JAN-DEC)')
            print(df[df['Month']==n])
        if op1==6:
            df=pd.read_csv('E:\\projects\\Yearly Sales Analysis project\\Yearlysales.csv')
            df.to_csv('E:\\projects\\Yearly Sales Analysis project\\Yearlysales_new.csv')
            print('Check the destined folder to get the duplicate file')
        if op1==7:
            print('Going to main menu')
            main_menu()
    else:
            print('The option you selected is wrong, Try again!')

# submenu2 for Data Analysis & Manipulation

def submenu2():
    op2=0
    while op2!=9:
        print('1. Delete a column')
        print('2. Insert a new row')
        print('3. Display top records')
        print('4. Display bottom records')
        print('5. Display lowest 3 Price')
        print('6. Display highest 3 Price')
        print('7. Sort Data in Descending order by Total Profit')
        print('8. Access a part of data by Slicing')
        print('9. Go back to main menu')
        print()
        op2=int(input('Enter choice for Data Analysis & Manipulation'))
        print()
        if op2==1:
            df=pd.read_csv('E:\\projects\\Yearly Sales Analysis project\\Yearlysales.csv')
            print(df.columns)
            c=input('Enter column name you want to delete')
            del df[c]
            print('Column',c,'deleted')
            print(df)
            df.to_csv('E:\\projects\\Yearly Sales Analysis project\\Yearlysales_del.csv')
            print('Updated file is saved in destined folder')
        if op2==2:
            df=pd.read_csv('E:\\projects\\Yearly Sales Analysis project\\Yearlysales.csv')
            df1=pd.DataFrame()
            column=df.columns
            print(column)
            print(df.head(1))
            list1=[]
            list2=eval(input('Enter the values in list form which are to be inserted'))
            s1=pd.Series(list2,index=df.columns)
            df1=df.append(s1,ignore_index=True)
            print('New Row inserted')
            print(df1)
            df1.to_csv('E:\\projects\\Yearly Sales Analysis project\\Yearlysales_add.csv')
            print('Updated file is saved in destined folder')
        if op2==3:
            df=pd.read_csv('E:\\projects\\Yearly Sales Analysis project\\Yearlysales.csv')
            n=int(input('How many rows you want to display from top?'))
            print(df.head(n))  
        if op2==4:
            df=pd.read_csv('E:\\projects\\Yearly Sales Analysis project\\Yearlysales.csv')
            n=int(input('How many rows you want to display from bottom?'))
            print(df.tail(n))
        if op2==5:
            df=pd.read_csv('E:\\projects\\Yearly Sales Analysis project\\Yearlysales.csv',usecols=['Month','Quarter','Total_units'])
            print(df.sort_values(by=['Total_units'],ascending=False).tail(3))
        if op2==6:
            df=pd.read_csv('E:\\projects\\Yearly Sales Analysis project\\Yearlysales.csv',usecols=['Month','Quarter','Total_units'])
            print(df.sort_values(by=['Total_units'],ascending=False).head(3))
        if op2==7:
            df=pd.read_csv('E:\\projects\\Yearly Sales Analysis project\\Yearlysales.csv',usecols=['Month','Total_profit'])
            print(df.sort_values(by=['Total_profit'],ascending=False))
        if op2==8:
            df=pd.read_csv('E:\\projects\\Yearly Sales Analysis project\\Yearlysales.csv')
            a=int(input('Enter the starting index of row'))
            b=int(input('Enter the ending index(end excluded) of row'))
            c=int(input('Enter the starting index of column'))
            d=int(input('Enter the ending index(end excluded) of column'))
            print('Displaying the sliced data')
            print(df.iloc[a:b,c:d])
        if op2==9:
            print('Going to main menu')
            main_menu()
    else:
            print('The option you selected is wrong, Try again!')


# submenu3 for Data Visualization
def submenu3():
    op3=0
    while op3!=7:
        print('1. Line Plot showing Month vs Total units sold in a year')
        print('2. Line Plot showing Month vs Facecream sales in a year')
        print('3. Bar Plot showing Month vs Total units sold in a year ')
        print('4. All in one Line plot for all products')
        print('5. All in one bar plot for all products')
        print('6. Horizontal Bar Plot for Venue vs Average no. of sixes')
        print('7. Go back to main menu')
        print()
        op3=int(input('Enter choice to Display Visualization'))
        print()
        if op3==1:
            df=pd.read_csv('E:\\projects\\Yearly Sales Analysis project\\Yearlysales.csv')
            u=df['Total_units']
            m=df['Month'] 
            plt.plot(m,u)
            plt.xlabel('Month')
            plt.ylabel('Total_units')
            plt.xticks(rotation='vertical')
            plt.title('Line Plot showing Month vs Total units sold in a year')
            plt.show()
            plt.savefig('E:\\projects\\Yearly Sales Analysis project\\fig1')
        if op3==2:
            df=pd.read_csv('E:\\projects\\Yearly Sales Analysis project\\Yearlysales.csv')
            f=df['Facecream']
            m=df['Month'] 
            plt.plot(m,f)
            plt.xlabel('Month')
            plt.ylabel('Facecream')
            plt.xticks(rotation='vertical')
            plt.title('Line Plot showing Month vs Facecream sales')
            plt.show()
        if op3==3:
            df=pd.read_csv('E:\\projects\\Yearly Sales Analysis project\\Yearlysales.csv')
            m=df['Month'] 
            u=df['Total_units']
            plt.bar(m,u)
            plt.xlabel('Month')
            plt.ylabel('Total_units')
            plt.xticks(rotation='vertical')
            plt.title('Bar Plot showing Month vs Total units sold in a year')
            plt.show()
        if op3==4:
            df=pd.read_csv('E:\\projects\\Yearly Sales Analysis project\\Yearlysales.csv')
            m=df['Month'] 
            f=df['Facecream']
            fw=df['Facewash']
            t=df['Toothpaste']
            b=df['Bathing_soap']
            s=df['Shampoo']
            mois=df['Moisturizer']
            u=df['Total_units']
            tp=df['Total_profit']
            plt.plot(m,f,label='Facecream')
            plt.plot(m,fw,label='Facewash')
            plt.plot(m,t,label='Toothpaste')
            plt.plot(m,b,label='Bathing_soap')
            plt.plot(m,s,label='Shampoo')
            plt.plot(m,mois,label='Moisturizer')
            plt.xlabel('Month')
            plt.ylabel('Products')
            plt.xticks(rotation='vertical')
            plt.title('All in one Line plot for all products')
            plt.legend()
            plt.show()
        if op3==5:
            df=pd.read_csv('E:\\projects\\Yearly Sales Analysis project\\Yearlysales.csv')
            m=df['Month'] 
            f=df['Facecream']
            fw=df['Facewash']
            t=df['Toothpaste']
            b=df['Bathing_soap']
            s=df['Shampoo']
            mois=df['Moisturizer']
            u=df['Total_units']
            tp=df['Total_profit']
            plt.bar(m,f,label='Facecream')
            plt.bar(m,fw,label='Facewash')
            plt.bar(m,t,label='Toothpaste')
            plt.bar(m,b,label='Bathing_soap')
            plt.bar(m,s,label='Shampoo')
            plt.bar(m,mois,label='Moisturizer')
            plt.xlabel('Season')
            plt.ylabel('Win by runs')
            plt.xticks(rotation='vertical')
            plt.title('All in one Line plot for all products')
            plt.legend()
            plt.show()
        if op3==6:
            df=pd.read_csv('E:\\projects\\Yearly Sales Analysis project\\Yearlysales.csv')
            m=df['Month'] 
            u=df['Total_units']
            plt.barh(m,u)
            plt.xlabel('Month')
            plt.ylabel('Total_units')
            plt.xticks(rotation='vertical')
            plt.title(' Horizontal Bar Plot showing Month vs Total units sold in a year')
            plt.show()
        if op3==7:
            print('Going to main menu')
            main_menu()
    else:
        print('Enter valid Choice')

# Main menu to call other sub menus
def main_menu():
    option=0
    while option!=4:
        print('****************************************************************************')
        print('                          WELCOME TO YEARLY SALES ANALYSIS SYSTEM        ')
        print('                                     **SUPER MEGA STORE**            ')
        print('****************************************************************************')
        print()
        print('1. Display Data')
        print('2. Data Analysis & Manipulation')
        print('3. Data Visualization')
        print('4. Exit')
        print()
        print('***************************************************************************')
        print()
        print()
        option=int(input('Choose an option from above options'))
        if option==1:
            submenu1()
        elif option==2:
            submenu2()
        elif option==3:
            submenu3()
        else:
            print('Thankyou for yor visit. Exiting...')
            exit()
            
main_menu()
