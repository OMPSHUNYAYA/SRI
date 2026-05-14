S = {
    "E": {"input": True, "ready": True},
    "C": [lambda s: s["E"].get("conflict") is True],
    "F": [lambda s: s["E"].get("context") is None],
    "R": [lambda s: s["E"].get("input") is True and s["E"].get("ready") is True],
    "P": []
}

def resolve(S):
    for c in S["C"]:
        if c(S):
            return "CONFLICT"
    for f in S["F"]:
        if f(S):
            return "INCOMPLETE"
    for p in S["P"]:
        if p(S):
            return "FORBIDDEN"
    for r in S["R"]:
        if not r(S):
            return "ABSTAIN"
    return "RESOLVED"

print(resolve(S))