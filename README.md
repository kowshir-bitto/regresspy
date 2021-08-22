# Regresspy 


A python library to implement regression model using Gradient Descent from scratch.

##How gradient descent works
Gradient descent is an iterative optimization algorithm for finding the local minimum of a function. To find the local minimum of a function using gradient descent, we must take steps proportional to the negative of the gradient (move away from the gradient) of the function at the current point.

##Step 1 
(Error function declaration) I used mae,sse,mse & rmse as error function to evaluate my model. You can find all function on loss.py file from regresspy main directory.

##Step 2 
(Forward & Bacward propagation) Forward Propagation is the way to move from the Input layer (left) to the Output layer (right) in the neural network. The process of moving from the right to left i.e backward from the Output to the Input layer is called the Backward Propagation. I declared those functions on gradient_descent.py file.

##Step 3
(Testing file creation) I used test_loss.py file to assert error functions on from my loss.py file. To do that I did generate dummy dataset and given a calculate value using hardcoding and then call separate function from loss.py file to see if they are working properly.

##Step 4 
(Regression class declaration) This is the heart of this library, all functions like train,fit,predict,score,initialize_weights are declared in a single class called Regression(). Point to be noted, we will use this function to be called on model.py file to run and see if our Regression class is working fine.

##Step 5 
(Running the model) If Regression class is the heart of this programme then this model.py file is the brain. In this case I called a scikit learn library and calculate rmse from there, in the mean time I called my Regression model and then calculate rmse using our own model that we built. Result were quit similar and package is ready.

##Conclusion 
It was quite good programme that I write on my academic career. Special thanks to my course teacher "Musabbir Hossain" who helped me a lot by giving basic structure of this package and fixing error when I was lost in the dark by facing some critical error on model.py file.
