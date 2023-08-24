from flask.views import MethodView
from wtforms import Form, StringField, SubmitField
from flask import Flask, render_template, request
from flatmates_bill import flat

app = Flask(__name__)


class HomePage(MethodView):

    def get(self):
        return render_template("index.html")


class BillFormPage(MethodView):
    def get(self):
        bill_form = BillForm()
        return render_template('bill_form_page.html',
                               billform=bill_form)


class ResultsPage(MethodView):

    def post(self):
        billform = BillForm(request.form)

        the_bill = flat.Bill(float(billform.amount.data), billform.period.data)
        flatmate1 = flat.Flatmate(billform.name1.data, float(billform.days_in_house1.data))
        flatmate2 = flat.Flatmate(billform.name2.data, float(billform.days_in_house2.data))

        return render_template("results.html", name1=flatmate1.name,
                               amount1=flatmate1.pays(the_bill, flatmate2),
                               name2=flatmate2.name,
                               amount2=flatmate2.pays(the_bill, flatmate1))


class BillForm(Form):
    amount = StringField("Bill Amounst: ", default="2000")
    period = StringField("Bill Period: ", default="December 2023")

    name1 = StringField("Name: ", default="Adrian")
    days_in_house1 = StringField("Days in the house: ", default="20")

    name2 = StringField("Name: ", default="Natalia")
    days_in_house2 = StringField("Days in the house: ", default="25")

    button = SubmitField("Calculate")


if __name__ == '__main__':
    app.add_url_rule('/', view_func=HomePage.as_view('home_page'))

    app.add_url_rule('/bill_form', view_func=BillFormPage.as_view('bill_form_page'))

    app.add_url_rule('/results', view_func=ResultsPage.as_view('results_page'))

    app.run(host='0.0.0.0')

