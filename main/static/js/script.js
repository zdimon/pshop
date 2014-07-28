// Generated by CoffeeScript 1.7.1
(function() {
  var app;

  app = angular.module('example.api', ['ngResource']);

  app.factory('Catalog', [
    '$resource', function($resource) {
      return $resource('/rest/catalog/?format=json');
    }
  ]);

  app = angular.module('example.app.static', ['example.api']);

  app.controller('AppController', [
    '$scope', 'Catalog', function($scope, Catalog) {
      return $scope.catalog = Catalog.query();
    }
  ]);

}).call(this);
