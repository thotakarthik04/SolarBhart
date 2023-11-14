from flask import Blueprint,render_template,request,flash
calc=Blueprint('calc',__name__)

@calc.route('/',methods=['GET','POST'])
def home():
    return render_template("index.html",boolean=True)

@calc.route('/Community',methods=['GET','POST'])
def community():
    return render_template("community.html",boolean=True)

@calc.route('/About',methods=['GET','POST'])
def about():
    return render_template("about.html",boolean=True)

@calc.route('/WhySolar',methods=['GET','POST'])
def why_solar():
    return render_template("whysolar.html",boolean=True)

@calc.route('/SolarCalculator',methods=['GET','POST'])
def calculator():
    if request.method=='POST':
        panel_capacity=request.form.get('panel_capacity')
        customer_category=request.form.get('customer_category')
        state=request.form.get('state')
        electricity_cost=request.form.get('electricity_cost')
        if panel_capacity=="":
            flash('Insufficient capacity',category='error')
        elif float(panel_capacity)==0 or float(panel_capacity)<0:
            flash('Insufficient capacity',category='error')
        elif float(panel_capacity)>10:
            flash('Sorry, No information at the present available for more than 10kW capacity for residential category.')
        elif customer_category=='0':
            flash('No Customer Category was selected',category='error')
        elif state=='select_state':
            flash('No State was selected',category='error')
        elif electricity_cost=='':
            flash('Electricity cost was not specified',category='error')
        elif float(electricity_cost)<0 or float(electricity_cost)==0:
            flash('Electricity cost must be greater than zero',category='error')
        else:
            north_eastern_ht=["arunachal_pradesh","assam","manipur","meghalaya","mizoram","nagaland","sikkim","tripura","uttarakhand","jammu_kashmir","lakshadweep","andaman_nicobar"]
            if state not in north_eastern_ht:
                if float(panel_capacity)<=3:
                    subsidy=14588*float(panel_capacity)
                elif float(panel_capacity)>3 and float(panel_capacity)<=10:
                    subsidy=(14588*3)+(7294*(float(panel_capacity)-3))
                else:
                    subsidy=(14588*3)+(7294*10)
            else:
                if float(panel_capacity)<=3:
                    subsidy=17662*float(panel_capacity)
                elif float(panel_capacity)>3 and float(panel_capacity)<=10:
                    subsidy=(17622*3)+(8831*(float(panel_capacity)-3))
                else:
                    subsidy=(17662*3)+(8831*10)
            electricity_cost=float(electricity_cost)
            solar_price_kw=[0,80000,150000,210000,280000,350000,400000,450000,500000,600000,700000]
            panel_capacity=round(float(panel_capacity))
            panel_price=solar_price_kw[panel_capacity]
            total_price=panel_price-subsidy
            per_month_savings=758.334*panel_capacity
            bill_amount=electricity_cost-per_month_savings
            flash("Subsidy=Rs."+str(round(subsidy)),category="success")
            if bill_amount>0:
                bill_saving=electricity_cost-bill_amount
                flash(", Monthly electricity bill=Rs."+str(round(bill_amount)),category="success")
            elif bill_amount<0:
                bill_saving=abs(bill_amount)
                flash(", Monthly electricity bill=Rs."+str(0),category="success")
            flash(", You will save Rs."+str(round(bill_saving))+" per month",category="success")
            month=0
            while bill_saving<=total_price:
                month+=1
                bill_saving=bill_saving+(electricity_cost-bill_amount)
            flash(", Payback period="+str(month)+" months",category="success")
    return render_template("solarcalculator.html",boolean=True)


