G := AbelianGroup([2, 2, 2, 2, 2, 2, 2, 2, 4, 4, 8]);
# G := AbelianGroup([2, 2, 4]);
orders := List(Elements(G), x -> Order(x));
freq := List(Set(orders), o -> Length(Filtered(orders, x -> x = o)));
Print(freq, "\n");
