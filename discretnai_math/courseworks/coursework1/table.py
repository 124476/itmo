import itertools


def diff_by_one_bit(s1, s2):
    diff_count = 0
    res = []
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            diff_count += 1
            res.append('X')
        else:
            res.append(s1[i])
    if diff_count == 1:
        return "".join(res)
    return None


def get_weight(s):
    return s.count('1')


def format_expr(term, vars_count=5):
    expr = []
    for i, char in enumerate(term):
        if char == '1':
            expr.append(f"x{i + 1}")
        elif char == '0':
            expr.append(f"!x{i + 1}")
    return " & ".join(expr) if expr else "1"


class QMTable:
    def __init__(self, minterms, dontcares, vars_count=5):
        self.vars_count = vars_count
        self.minterms = minterms
        self.dontcares = dontcares
        # Объединяем и сортируем для K0
        all_terms = sorted(list(set(minterms + dontcares)))
        self.K0 = [{'bin': bin(x)[2:].zfill(vars_count), 'val': x, 'merged': False, 'idx': i + 1, 'sources': []} for
                   i, x in enumerate(all_terms)]

        self.K1 = []
        self.K2 = []
        self.K3 = []
        self.Z = []

    def process_level(self, current_level, next_level, level_name):
        """Склеивает кубы текущего уровня"""
        groups = {}
        for term in current_level:
            w = get_weight(term['bin'])
            if w not in groups: groups[w] = []
            groups[w].append(term)

        merged_dict = {}

        for w in range(self.vars_count):
            if w in groups and (w + 1) in groups:
                for t1 in groups[w]:
                    for t2 in groups[w + 1]:
                        combined = diff_by_one_bit(t1['bin'], t2['bin'])
                        if combined:
                            t1['merged'] = True
                            t2['merged'] = True
                            source_pair = (t1['idx'], t2['idx'])

                            if combined not in merged_dict:
                                merged_dict[combined] = {'bin': combined, 'merged': False, 'sources': []}
                            merged_dict[combined]['sources'].append(source_pair)

        next_level_list = []
        for i, (k, v) in enumerate(sorted(merged_dict.items())):
            v['idx'] = i + 1
            next_level_list.append(v)

        return next_level_list

    def build_all_levels(self):
        self.K1 = self.process_level(self.K0, self.K1, "K1")
        self.K2 = self.process_level(self.K1, self.K2, "K2")
        self.K3 = self.process_level(self.K2, self.K3, "K3")

        for level in [self.K0, self.K1, self.K2, self.K3]:
            for term in level:
                if not term['merged']:
                    self.Z.append(term['bin'])

    def print_table(self):
        print("\n" + "=" * 80)
        print(f"{'K^0(f) ∪ N(f)':<20} | {'K^1(f)':<25} | {'K^2(f)':<25} | {'K^3(f)':<10} | {'Z(f)'}")
        print("=" * 80)

        # Находим максимальную длину для каждой колонки, чтобы красиво выровнять
        max_rows = max(len(self.K0), len(self.K1), len(self.K2), max(len(self.K3), 1))

        def fmt_term(t, is_z=False):
            if not t: return ""
            if is_z: return t
            v = " v" if t['merged'] else ""
            src = ""
            if t['sources']:
                src = " " + " ".join(f"({s[0]}-{s[1]})" for s in t['sources'])
            return f"{t['idx']}. {t['bin']}{src}{v}"

        for i in range(max_rows):
            c0 = fmt_term(self.K0[i]) if i < len(self.K0) else ""
            c1 = fmt_term(self.K1[i]) if i < len(self.K1) else ""
            c2 = fmt_term(self.K2[i]) if i < len(self.K2) else ""
            c3 = fmt_term(self.K3[i]) if i < len(self.K3) else ""
            cz = self.Z[i] if i < len(self.Z) else ""

            print(f"{c0:<20} | {c1:<25} | {c2:<25} | {c3:<10} | {cz}")

        print("=" * 80)
        print(f"K^4(f) = ∅\n")

    def get_minimal_cover(self):
        best_cover = None
        best_cost = float('inf')

        useful_Z = []
        for z in self.Z:
            covers_one = False
            for m in self.minterms:
                m_bin = bin(m)[2:].zfill(5)
                match = True
                for j in range(5):
                    if z[j] != 'X' and z[j] != m_bin[j]:
                        match = False;
                        break
                if match: covers_one = True; break
            if covers_one:
                useful_Z.append(z)

        for r in range(1, len(useful_Z) + 1):
            for combo in itertools.combinations(useful_Z, r):
                covered = set()
                for p in combo:
                    for m in self.minterms:
                        m_bin = bin(m)[2:].zfill(5)
                        match = True
                        for j in range(5):
                            if p[j] != 'X' and p[j] != m_bin[j]:
                                match = False;
                                break
                        if match: covered.add(m)

                if len(covered) == len(self.minterms):
                    cost = sum((5 - p.count('X')) + 1 for p in combo)
                    if cost < best_cost:
                        best_cost = cost
                        best_cover = list(combo)
        return best_cover, best_cost


minterms = [5, 6, 7, 12, 13, 14, 15, 19, 20, 21, 22, 27, 28, 29]
dontcares = [2, 10, 18, 26]

qm = QMTable(minterms, dontcares)
qm.build_all_levels()
qm.print_table()

cover, cost = qm.get_minimal_cover()

print("--- РЕЗУЛЬТАТ ---")
print("Минимальное покрытие (МДНФ):")
print("  f = " + "  v  ".join([f"({format_expr(p)})" for p in cover]))
print(f"\nЦена по Квайну (S^b): {cost}")