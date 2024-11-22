import numpy as np

def sigmoid(z):
    return 1/(1 + np.exp(-z))

def random_weights(network_composition):
    weights = []
    for i in range(len(network_composition)-1):
        layer_node_count = network_composition[i+1]
        prev_layer_node_count = network_composition[i]
        weights.append(np.random.rand(layer_node_count, prev_layer_node_count))

    return weights

def random_biases(network_composition):
    weights = []
    for i in range(len(network_composition)-1):
        layer_node_count = network_composition[i+1]
        prev_layer_node_count = network_composition[i]
        weights.append(np.random.rand(layer_node_count, prev_layer_node_count))

    return weights

def random_binary_input(network_composition):
    inputs = np.random.randint(2, network_composition[0])
    return inputs

def propagate_network (inputs, weights, biases, network_composition=None):
    if network_composition == None :
        network_composition = [len(inputs)]
        for layer in range(len(weights)):
            network_composition.append(len(weights[layer]))

    for layer, nodes in enumerate(network_composition[1:]):
        outputs = []
        neruron_values = []
        for node in range(nodes):
            # print(f"node: {node}, inputs: {len(inputs)}, nodes: {nodes}, weights: {len(weights[layer])}, {len(weights[layer][node])}")
            outputs.append(
                sigmoid(
                    np.average(
                        np.multiply(inputs, weights[layer][node])+biases[layer][node]
                    )
                )
            )

        neruron_values.append(outputs)

        inputs = outputs

    return outputs

def train_xor(inputs, weights, biases, network_composition=None):
    if network_composition == None :
        network_composition = [len(inputs)]
        for layer in range(len(weights)):
            network_composition.append(len(weights[layer]))

    network_error = []
    for i in range(100):
        inputs = np.random.randint(2, network_composition[0])
        output = propagate_network(inputs,weights,baises,network_composition)   

        error = np.power(output - xor(*inputs),2)

        network_error.append(sum(error))



def xor(a,b):
    return int(a+b == 1)


network_composition = [2,10,10,1] # number of nodes in each network layer

# Initial values
weights=random_weights(network_composition)
baises=random_biases(network_composition)



print()
