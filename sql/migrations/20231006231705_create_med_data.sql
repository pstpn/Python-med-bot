-- +goose Up
-- +goose StatementBegin
CREATE TABLE IF NOT EXISTS public.overdue
(
    subject          text NOT NULL check ( subject != '' ),
    mo               text NOT NULL check ( mo != '' ),
    tax_id           text NOT NULL check ( tax_id > '' ),
    status           text NOT NULL check ( Status != '' ),
    withdrawal_type  text NOT NULL check ( withdrawal_type != '' ),
    gtin             text NOT NULL check ( gtin  != '' ),
    batch            text NOT NULL check ( batch != '' ),
    doses_in_package int NOT NULL check ( doses_in_package >= 0 ),
    packages_count   int NOT NULL check ( packages_count >= 0 ),
    doses_count      int NOT NULL check ( doses_count >= 0 ),
    ex_date          date NOT NULL,
    ex_days          int NOT NULL check ( ex_days > 0 )
);
-- +goose StatementEnd

-- +goose Down
-- +goose StatementBegin
DROP TABLE IF EXISTS public.overdue;
-- +goose StatementEnd
