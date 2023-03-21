import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt

#All graphs are trapezoidal
def plot_membership_functions_3_alltrapezoidal(title, xlabel, x_range, set1, set2, set3, set1_name, set2_name, set3_name):
    # Define the input variable range
    x = np.arange(*x_range)

    # Define the fuzzy sets for the input variable
    set1_values = fuzz.trapmf(x, set1)
    set2_values = fuzz.trapmf(x, set2)
    set3_values = fuzz.trapmf(x, set3)

    # Plot the membership functions for the input variable
    plt.figure(figsize=(8, 4))
    plt.plot(x, set1_values, 'b', linewidth=1.5, label=set1_name)
    plt.plot(x, set2_values, 'g', linewidth=1.5, label=set2_name)
    plt.plot(x, set3_values, 'r', linewidth=1.5, label=set3_name)
    plt.title(title)
    plt.yticks(np.arange(0, 1.1, 0.5))
    #plt.xlabel(xlabel)
    plt.legend()
    plt.show()

#Edges are traperzoidal, middle section is triagle
def plot_membership_functions_3(title, xlabel, x_range, set1, set2, set3, set1_name, set2_name, set3_name):
    # Define the input variable range
    x = np.arange(*x_range)

    # Define the fuzzy sets for the input variable
    set1_values = fuzz.trapmf(x, set1)
    set2_values = fuzz.trimf(x, set2)
    set3_values = fuzz.trapmf(x, set3)

    # Plot the membership functions for the input variable
    plt.figure(figsize=(8, 4))
    plt.plot(x, set1_values, 'b', linewidth=1.5, label=set1_name)
    plt.plot(x, set2_values, 'g', linewidth=1.5, label=set2_name)
    plt.plot(x, set3_values, 'r', linewidth=1.5, label=set3_name)
    plt.title(title)
    plt.yticks(np.arange(0, 1.1, 0.5))
    #plt.xlabel(xlabel)
    plt.legend()
    plt.show()

#Edges are traperzoidal, middle section is triagle
def plot_membership_functions_4(title, xlabel, x_range, set1, set2, set3, set4, set1_name, set2_name, set3_name, set4_name):
    # Define the input variable range
    x = np.arange(*x_range)

    # Define the fuzzy sets for the input variable
    set1_values = fuzz.trapmf(x, set1)
    set2_values = fuzz.trimf(x, set2)
    set3_values = fuzz.trimf(x, set3)
    set4_values = fuzz.trapmf(x, set4)

    # Plot the membership functions for the input variable
    plt.figure(figsize=(8, 4))
    plt.plot(x, set1_values, 'b', linewidth=1.5, label=set1_name)
    plt.plot(x, set2_values, 'g', linewidth=1.5, label=set2_name)
    plt.plot(x, set3_values, 'r', linewidth=1.5, label=set3_name)
    plt.plot(x, set4_values, 'm', linewidth=1.5, label=set4_name)
    plt.title(title)
    plt.yticks(np.arange(0, 1.1, 0.5))
    #plt.xlabel(xlabel)
    plt.legend(loc='center left')
    plt.show()


plot_membership_functions_3('Kambario dydis', 'kvadratiniai metrai', [0, 180], [0, 0, 15, 30], [20, 45, 60], [50, 90, 180, 180], "Mažas", "Vidutinis", "Didelis")
plot_membership_functions_3('Atstumas nuo miesto centro', 'kilometrai', [0, 40], [0, 0, 3, 8], [6, 14, 22], [18, 30, 40, 40], "Artimas", "Vidutinis", "Tolimas")
plot_membership_functions_4('Klientų įvertinimas', 'įvertis', [0, 11], [0, 0, 2, 5], [4, 5, 7], [6, 8, 9], [8, 10, 10, 10], "Nepatenkinamas", "Patenkinamas", "Geras", "Puikus")
plot_membership_functions_3_alltrapezoidal('Kambario kaina', 'EUR', [20, 200], [20, 20, 50, 85], [50, 70, 100 , 120], [85, 150, 200, 200], "Pigi", "Vidutinė", "Brangi")
