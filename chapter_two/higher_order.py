# Combine two tuples, filter for digits, return set
def restore_documents(originals, backups):
    return(
        set(
            filter(
                lambda txt : not txt.isdigit(), map(str.upper, originals + backups)
            )
        )
    )
