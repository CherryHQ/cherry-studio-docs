---
icon: cloud-binary
---
# S3 Συμβατή Αποθήκευση Αντιγράφων Ασφαλείας


{% hint style="warning" %}
Αυτό το έγγραφο μεταφράστηκε από τα Κινεζικά με AI και δεν έχει ακόμη ελεγχθεί.
{% endhint %}




Το Cherry Studio υποστηρίζει αντίγραφα ασφαλείας δεδομένων μέσω συμβατής αποθήκευσης S3 (αποθήκευση αντικειμένων). Κοινές υπηρεσίες συμβατής αποθήκευσης S3 περιλαμβάνουν: AWS S3, Cloudflare R2, Alibaba Cloud OSS, Tencent Cloud COS και MinIO.

Με βάση τη συμβατή αποθήκευση S3, μπορείτε να συγχρονίσετε δεδομένα πολλαπλών συσκευών με τον τρόπο:  
`A电脑` $$\xrightarrow{\text{αντίγραφο ασφαλείας}}$$ `S3存储` $$\xrightarrow{\text{αποκατάσταση}}$$ `B电脑`

### Ρύθμιση Συμβατής Αποθήκευσης S3

1.  Δημιουργήστε έναν κάδο αποθήκευσης αντικειμένων (Bucket) και καταγράψτε το όνομά του. **Συνιστάται ιδιαίτερα να ορίσετε τον κάδο ως ιδιωτικό για ανάγνωση/εγγραφή για την αποφυγή διαρροής δεδομένων αντιγράφου ασφαλείας!!**
2.  Ανατρέξτε στην τεκμηρίωση και μεταβείτε στην κονσόλα υπηρεσιών cloud για να λάβετε πληροφορίες όπως:
    - **Endpoint**: Η διεύθυνση πρόσβασης για τη συμβατή αποθήκευση S3, συνήθως με τη μορφή `https://<bucket-name>.<region>.amazonaws.com` ή `https://<ACCOUNT_ID>.r2.cloudflarestorage.com`.
    - **Region**: Η περιοχή όπου βρίσκεται ο κάδος, π.χ. `us-west-1`, `ap-southeast-1` κ.λπ. Για Cloudflare R2 εισάγετε `auto`.
    - **Bucket**: Το όνομα του κάδου.
    - **Access Key ID** και **Secret Access Key**: Τα διαπιστευτήρια για την πιστοποίηση.
    - **Root Path**: Προαιρετικό, καθορίζει τη ρίζα διαδρομής κατά το αντίγραφο ασφαλείας στον κάδο (προεπιλογή: κενό).
    - **Σχετική Τεκμηρίωση**
      - AWS S3: [Λήψη Access Key ID και Secret Access Key](https://docs.aws.amazon.com/zh_cn/IAM/latest/UserGuide/id_credentials_access-keys.html)
      - Cloudflare R2: [Λήψη Access Key ID και Secret Access Key](https://developers.cloudflare.com/r2/api/tokens/)
      - Alibaba Cloud OSS: [Λήψη Access Key ID και Access Key Secret](https://help.aliyun.com/zh/oss/developer-reference/use-amazon-s3-sdks-to-access-oss#306596478ed3r)
      - Tencent Cloud COS: [Λήψη SecretId και SecretKey](https://cloud.tencent.com/document/product/436/37421)
3.  Στις ρυθμίσεις αντιγράφου ασφαλείας S3, συμπληρώστε τις παραπάνω πληροφορίες. Κάντε κλικ στο κουμπί "Αντίγραφο ασφαλείας" για να ξεκινήσετε το αντίγραφο ασφαλείας ή στο κουμπί "Διαχείριση" για προβολή και διαχείριση της λίστας αρχείων αντιγράφου ασφαλείας.