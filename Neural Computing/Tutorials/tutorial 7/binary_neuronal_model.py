import numpy as np

def random_weights(network_composition):
    weights = []
    for i in range(len(network_composition)-1):
        layer_node_count = network_composition[i+1]
        prev_layer_node_count = network_composition[i]
        weights.append(np.random.rand(layer_node_count, prev_layer_node_count))

    return weights

def random_input(network_composition):
    inputs = np.random.rand(network_composition[0])
    return inputs

def propagate_network (inputs, weights, network_composition=None):
    if network_composition == None :
        network_composition = [len(inputs)]
        for layer in range(len(weights)):
            network_composition.append(len(weights[layer]))

    for layer, nodes in enumerate(network_composition[1:]):
        outputs = []
        for node in range(nodes):
            # print(f"node: {node}, inputs: {len(inputs)}, nodes: {nodes}, weights: {len(weights[layer])}, {len(weights[layer][node])}")
            outputs.append(
                np.average(
                    np.multiply(inputs, weights[layer][node])
                )
            )

        inputs = outputs

    return outputs

network_composition = [10,20,20,4] # number of nodes in each network layer

print(propagate_network(random_input(network_composition),random_weights(network_composition),network_composition))
