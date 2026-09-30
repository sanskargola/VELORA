from alembic import op
import sqlalchemy as sa


def upgrade() -> None:
    op.create_table(
        'users',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('email', sa.String(length=255), nullable=False),
        sa.Column('password_hash', sa.String(length=255), nullable=False),
        sa.Column('role', sa.Enum('admin', 'user', name='user_role'), nullable=True),
        sa.Column('is_verified', sa.Boolean(), nullable=True),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_index(op.f('ix_users_id'), 'users', ['id'], unique=False)

    op.create_table(
        'stocks',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('symbol', sa.String(length=16), nullable=False),
        sa.Column('company_name', sa.String(length=255), nullable=False),
        sa.Column('sector', sa.String(length=128), nullable=True),
        sa.Column('market_cap', sa.BigInteger(), nullable=True),
        sa.Column('currency', sa.String(length=8), nullable=True),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_stocks_id'), 'stocks', ['id'], unique=False)
    op.create_index(op.f('ix_stocks_symbol'), 'stocks', ['symbol'], unique=True)

    op.create_table(
        'historical_prices',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('stock_id', sa.Integer(), nullable=False),
        sa.Column('price_date', sa.Date(), nullable=False),
        sa.Column('open_price', sa.Numeric(precision=12, scale=4), nullable=False),
        sa.Column('high_price', sa.Numeric(precision=12, scale=4), nullable=False),
        sa.Column('low_price', sa.Numeric(precision=12, scale=4), nullable=False),
        sa.Column('close_price', sa.Numeric(precision=12, scale=4), nullable=False),
        sa.Column('volume', sa.Integer(), nullable=True),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
        sa.ForeignKeyConstraint(['stock_id'], ['stocks.id']),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('stock_id', 'price_date', name='uq_stock_price_date')
    )

    op.create_table(
        'predictions',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('stock_id', sa.Integer(), nullable=False),
        sa.Column('model_name', sa.String(length=64), nullable=False),
        sa.Column('predicted_price', sa.Numeric(precision=12, scale=4), nullable=False),
        sa.Column('confidence_score', sa.Numeric(precision=6, scale=4), nullable=False),
        sa.Column('recommendation', sa.String(length=16), nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
        sa.ForeignKeyConstraint(['stock_id'], ['stocks.id']),
        sa.ForeignKeyConstraint(['user_id'], ['users.id']),
        sa.PrimaryKeyConstraint('id')
    )

    op.create_table(
        'prediction_history',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('prediction_id', sa.Integer(), nullable=False),
        sa.Column('recorded_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
        sa.Column('predicted_price', sa.Numeric(precision=12, scale=4), nullable=False),
        sa.Column('confidence_score', sa.Numeric(precision=6, scale=4), nullable=False),
        sa.Column('recommendation', sa.String(length=16), nullable=False),
        sa.ForeignKeyConstraint(['prediction_id'], ['predictions.id']),
        sa.PrimaryKeyConstraint('id')
    )

    op.create_table(
        'portfolio',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('stock_id', sa.Integer(), nullable=False),
        sa.Column('quantity', sa.Numeric(precision=12, scale=4), nullable=False),
        sa.Column('average_buy_price', sa.Numeric(precision=12, scale=4), nullable=False),
        sa.Column('current_price', sa.Numeric(precision=12, scale=4), nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
        sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
        sa.ForeignKeyConstraint(['stock_id'], ['stocks.id']),
        sa.ForeignKeyConstraint(['user_id'], ['users.id']),
        sa.PrimaryKeyConstraint('id')
    )

    op.create_table(
        'watchlist',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('stock_id', sa.Integer(), nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
        sa.ForeignKeyConstraint(['stock_id'], ['stocks.id']),
        sa.ForeignKeyConstraint(['user_id'], ['users.id']),
        sa.PrimaryKeyConstraint('id')
    )

    op.create_table(
        'transactions',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('stock_id', sa.Integer(), nullable=False),
        sa.Column('transaction_type', sa.String(length=16), nullable=False),
        sa.Column('quantity', sa.Numeric(precision=12, scale=4), nullable=False),
        sa.Column('price_per_unit', sa.Numeric(precision=12, scale=4), nullable=False),
        sa.Column('total_amount', sa.Numeric(precision=12, scale=4), nullable=False),
        sa.Column('transaction_date', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
        sa.ForeignKeyConstraint(['stock_id'], ['stocks.id']),
        sa.ForeignKeyConstraint(['user_id'], ['users.id']),
        sa.PrimaryKeyConstraint('id')
    )

    op.create_table(
        'news',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('title', sa.String(length=255), nullable=False),
        sa.Column('content', sa.Text(), nullable=False),
        sa.Column('source', sa.String(length=128), nullable=False),
        sa.Column('url', sa.String(length=512), nullable=True),
        sa.Column('published_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )

    op.create_table(
        'technical_indicators',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('stock_id', sa.Integer(), nullable=False),
        sa.Column('indicator_name', sa.String(length=64), nullable=False),
        sa.Column('indicator_value', sa.Numeric(precision=12, scale=4), nullable=False),
        sa.Column('indicator_date', sa.Date(), nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
        sa.ForeignKeyConstraint(['stock_id'], ['stocks.id']),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade() -> None:
    op.drop_table('technical_indicators')
    op.drop_table('news')
    op.drop_table('transactions')
    op.drop_table('watchlist')
    op.drop_table('portfolio')
    op.drop_table('prediction_history')
    op.drop_table('predictions')
    op.drop_table('historical_prices')
    op.drop_table('stocks')
    op.drop_table('users')
