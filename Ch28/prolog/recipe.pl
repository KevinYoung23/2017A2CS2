/*facts*/
vegetable(carrot).
vegetable(lettuce).
meat(chicken).
meat(beef).
ingredient(carrot, salad, 100).
ingredient(beef, chickensoup, 700).
/*rules*/
containsmeat(X) : -
         ingredient(Y, X, _).
         meat(Y).
