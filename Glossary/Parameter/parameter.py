
def sum(x):
    return x + x


# positional-or-keyword parameter
def positional_or_keyword_funciton(x):
    return x + x


print(positional_or_keyword_funciton(x=5))
print(positional_or_keyword_funciton(5))


# positional-only parameter
def positional_only_function(x, /):
    return x + x


# error code
# print(positional_only_function(x=5))
print(positional_only_function(5))


# keyword-only parameter
def keyword_only_function(*, x):
    return x + x


print(keyword_only_function(x=5))
# error code
# print(keyword_only_function(5))


# var-positional parameter
def var_positional_function(*args):
    return args


print(var_positional_function(1, 2, 3, 4, 5))


# var-keyword parameter
def var_keyword_function(**kwargs):
    return kwargs


print(var_keyword_function(kwargs=(1, 2, 3, 4, 5)))
