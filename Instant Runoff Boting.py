def runoff(voters):
    voter_dict = {k: 0 for k in voters[0]}

    for voter in voters:
        top_vote = voter[0]
        voter_dict[top_vote] += 1

    half_votes = len(voters) / 2
    for candidate, vote_number in voter_dict.items():
        if vote_number > half_votes:
            return candidate

    vote_tallies = [v for _, v in voter_dict.items()]
    least_votes = min(vote_tallies)
    least_votes = [k for k, v in voter_dict.items() if v == least_votes]
    if len(least_votes) == len(voter_dict):
        return None

    for voter in voters:
        for least in least_votes:
            voter.remove(least)

    return runoff(voters)


if __name__ == "__main__":
    print(runoff([["dem", "ind", "rep"],
                  ["rep", "ind", "dem"],
                  ["ind", "dem", "rep"],
                  ["ind", "rep", "dem"]]) == 'ind')

    print(runoff([["a", "c", "d", "e", "b"],
                  ["e", "b", "d", "c", "a"],
                  ["d", "e", "c", "a", "b"],
                  ["c", "e", "d", "b", "a"],
                  ["b", "e", "a", "c", "d"]]) is None)

    print(runoff([['Drake Luft', 'Johan Liebert', 'Abelt Dessler', 'Daisuke Aramaki'],
                  ['Drake Luft', 'Abelt Dessler', 'Johan Liebert', 'Daisuke Aramaki'],
                  ['Daisuke Aramaki', 'Drake Luft', 'Abelt Dessler', 'Johan Liebert'],
                  ['Abelt Dessler', 'Johan Liebert', 'Drake Luft', 'Daisuke Aramaki'],
                  ['Daisuke Aramaki', 'Johan Liebert', 'Drake Luft', 'Abelt Dessler'],
                  ['Abelt Dessler', 'Johan Liebert', 'Drake Luft', 'Daisuke Aramaki'],
                  ['Daisuke Aramaki', 'Abelt Dessler', 'Johan Liebert', 'Drake Luft'],
                  ['Daisuke Aramaki', 'Johan Liebert', 'Drake Luft', 'Abelt Dessler']]) == "Daisuke Aramaki")
