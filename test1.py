from sklearn.externals import joblib
model = joblib.load('model_cuisine_ingredients.pkl')

steak_hache = "1 tbsp vegetable oil 4 shallots  , very finely chopped 600g freshly ground beef   (ask the butcher for something with roughly 15% fat - we used chuck) 8 thyme sprigs, leaves picked and chopped 2 tsp Dijon mustard 2 tbsp plain flour 200ml crème fraîche 1 egg yolk 6 tarragon   sprigs, leaves picked and finely chopped dressed green salad, to serve"

pred = model.predict([steak_hache])[0]
print(pred)
