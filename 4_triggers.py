from datas.connect import conn

cursor = conn.cursor()

#Faire en sorte que les tables REGIONS et DEPARTEMENTS ne soit pas modifiables.
#Il faut bloquer les commandes INSERT, UPDATE et DELETE.
query5 = """
REVOKE INSERT, UPDATE, DELETE ON Region FROM PUBLIC;
"""
query6 = """
REVOKE INSERT, UPDATE, DELETE ON Departement FROM PUBLIC;
"""
cursor.execute(query5)
cursor.execute(query6)

#Ajoutez un trigger qui utilise la procédure stockée précédente pour mettre à jour 
#la population d'un département/région quand la population d'une ville est mise à jour.

query7 = """
CREATE OR REPLACE FUNCTION maj_pop()
RETURNS TRIGGER AS $$
BEGIN
    IF TG_TABLE_NAME = 'Pop_Commune' THEN
        PERFORM calcul_pop_dep_reg2();
    END IF;
    RETURN NULL;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_maj_pop
AFTER INSERT OR UPDATE OR DELETE ON Pop_Commune
FOR EACH STATEMENT EXECUTE FUNCTION maj_pop();
"""
cursor.execute(query7) 

## jsp comment tester si ça marche genre il faudrait faire une modif et voir si ça fait bien les maj ??

conn.commit()
conn.close()