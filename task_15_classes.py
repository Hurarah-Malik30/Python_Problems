class set_solution:

    def subsetsRecur(self, current, sset):
        if sset:
            return self.subsetsRecur(current, sset[1:]) + self.subsetsRecur(current + [sset[0]], sset[1:])
        return [current]

    def sub_sets(self,sset):
        return self.subsetsRecur([], sorted(sset))
        

print(set_solution().sub_sets([4,5,6]))