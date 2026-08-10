class Solution:
    def applySubstitutions(self, replacements: List[List[str]], text: str) -> str:
        replacementMap = {key: value for key, value in replacements}
        resolved = {}

        def resolveReplacement(key: str, val: str) -> None:
            nonlocal replacementMap, resolved
            if key in resolved:
                return

            i = 0
            resolvedVal = []
            while i < len(val):
                c = val[i]
                if c == "%":
                    keyToResolve = val[i + 1]
                    resolveReplacement(keyToResolve, replacementMap[keyToResolve])
                    resolvedVal.append(resolved[keyToResolve])
                    i += 3
                else:
                    resolvedVal.append(c)
                    i += 1

            resolved[key] = "".join(resolvedVal)

        for key, val in replacementMap.items():
            resolveReplacement(key, val)
            text = text.replace(f"%{key}%", resolved[key])

        return text
