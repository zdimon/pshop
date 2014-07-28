app = angular.module 'example.api', ['ngResource']

app.factory 'Catalog', ['$resource', ($resource) ->
    $resource '/rest/catalog/?format=json'
]

app = angular.module 'example.app.static', ['example.api']

app.controller 'AppController', ['$scope', 'Catalog', ($scope, Catalog) ->
    $scope.catalog = Catalog.query()
]
