from typing import Optional
from datetime import datetime, timezone
import sqlalchemy as sa
import sqlalchemy.orm as so
from app import db

from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    # __tablename__ = 'users'

    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    username: so.Mapped[str] = so.mapped_column(sa.String(64), index=True, unique=True)
    email: so.Mapped[Optional[str]] = so.mapped_column(sa.String(64), index=True, unique=True)
    pasword_hash: so.Mapped[Optional[str]] = so.mapped_column(sa.String(256))
    posts: so.WriteOnlyMapped['Post'] = so.relationship(back_populates='author')

    def __repr__(self):
        return '<user {}>'.format(self.username)
    
    def set_password(self, password):
        self.pasword_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.pasword_hash, password)
    
class Post(db.Model):
    # __tablename__ = 'posts'
    
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    body: so.Mapped[str] = so.mapped_column(sa.String(140))
    timestamp: so.Mapped[datetime] = so.mapped_column(index=True, default=lambda: datetime.now(timezone.utc))
    user_id: so.Mapped[int] = so.mapped_column(sa.ForeignKey(User.id), index=True)
    author: so.Mapped[User] = so.relationship(back_populates='posts')

    def __repr__(self):
        return '<Post {}>'.format(self.body)
                                        
