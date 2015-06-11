var app = angular.module('PizzaApp');

app.controller('PizzaController', ['$scope', 'PizzaFactory', function($scope, PizzaFactory){
    $scope.pizzaList =  function(){
        PizzaFactory.getAllPizzas().success(function(data){
            $scope.pizzas = data;
        }).error(function(data, status){
            console.log("Error: ", data, status);
        })
   }
   $scope.pizzaForm = function(pizza){
        $scope.pizzaName = pizza;
   }
   $scope.pizzaOrder = function(){
        
   }
}])
