import json

data = json.load(open('forJson.json'))

class DFA:
    current_state = None;

    def __init__(self, states, alphabet, transition_function, start_state, accept_states):
        self.states = states;
        self.alphabet = alphabet;
        self.transition_function = transition_function;
        self.start_state = start_state;
        self.accept_states = accept_states;
        self.current_state = start_state;
        return;

    def transition_to_state_with_input(self, input_value):
        if ((self.current_state, input_value) not in self.transition_function.keys()):
            self.current_state = None;
            return;
        self.current_state = self.transition_function[(self.current_state, input_value)];
        return;

    def in_accept_state(self):
        return self.current_state in accept_states;

    def go_to_initial_state(self):
        self.current_state = self.start_state;
        return;

    def run_with_input_list(self, input_list):
        self.go_to_initial_state();
        for inp in input_list:
            self.transition_to_state_with_input(inp);
            continue;
        return self.in_accept_state();

    pass;

states = set(data["states"])

alphabet = set(data["alphabet"])

start_state = data["start_state"]

accept_states = set(data["accept_states"])

tf = dict()
for i in data["tf"]:
    tf[i["current_state"], i["symbol"]] = i["new_state"]

d = DFA(states, alphabet, tf, start_state, accept_states);

with open("inputs.txt") as fp:
    for i, line in enumerate(fp):
        input_program = list(line)
        if '\n' in input_program:
            input_program.remove('\n')
        print_input = ''.join(str(x) for x in input_program)
        print("For input: " + print_input + ", Output is :" + str(d.run_with_input_list(input_program)))