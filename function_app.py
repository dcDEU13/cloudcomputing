import azure.functions as func
import logging

from prediction import make_prediction

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

@app.route(route="predictv1")
def predictv1(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    tenure = req.params.get("tenure")
    monthly = req.params.get("monthly")
    techsupport = req.params.get("techsupport")

    if tenure and monthly and techsupport:
        prediction = make_prediction(7
                                     tenure = float(tenure),
                                     MonthlyCharges = float(monthly),
                                     TechSupport_yes = float(techsupport))
        
        return func.HttpResponse(f"Hello, the predicition is {prediction}.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a tenure, monthly, and tech support in the query string or in the request body for a personalized response.",
             status_code=200
        )