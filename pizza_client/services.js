var pizzaServices = angular.module('PizzaApp');

pizzaServices.factory('PizzaFactory', ['$http', function($http){
    return {
        getAllPizzas: function(){
            return $http.get('http://localhost:8000/pizzas')
        },
        createPizza: function(data){
            return $http.post('http://localhost:8000/pizzas', data)
        },
        getPizza: function(name){
            return $http.get('http://localhost:8000/pizzas/' + name)
        },
        editPizza: function(data){
            return $http.put('http://localhost:8000/pizzas/:name', data)
        },
        deletePizza: function(data){
            return $http.delete('http://localhost:8000/pizzas/:name', data)
        }
    }
}])