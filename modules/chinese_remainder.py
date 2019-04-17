from functools import reduce

def chinese_remainder(number_values, mod_values, verbose=False):
    M = reduce((lambda x, y: x * y), mod_values)
    m_subs = list(map((lambda x: M/x), mod_values))
    y_subs = []
    for i in range(len(m_subs)):
        y_subs.append(int(multiplicative_inverse(m_subs[i], mod_values[i])))
    x = 0
    x_calc_string = 'Calculating X as '
    for i in range(len(number_values)):
        x += number_values[i]*m_subs[i]*y_subs[i]
        x_calc_string += str(number_values[i]) + ' * ' + str(m_subs[i]) + ' * ' + str(y_subs[i]) + ' + '
    x = int(x%M)
    if verbose:
        print('Calculating M as: ' + '*'.join(map(str, mod_values)) + ' = ' + str(M))
        print('Calculating M sub 1, ..., M sub N as ' + ','.join(map(str, m_subs)))
        print ('Calculating Y sub 1, ...., Y sub N as ' + ','.join(map(str, y_subs)))
        x_calc_string = x_calc_string[:-3]
        print (x_calc_string + ' = ' + str(x))
    return x

registerFunction("chinese_remainder", {
    "name" : "Solves chinese remainder theorem for a set of congruences",
    "arguments_short":["number_values","mod_values","verbose=False"],
    "arguments":["The number values of the problem in a list (i.e. for x = 14 mod 29 you'd put 4)", "The mod values of the problem in a list"],
    "description":"Returns the solution to a set of congruences using chinease remainder theorem"
})